from typing import Any, Dict, List
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
import mlflow
from prefect import task,flow


@task
def load_data(path: str) -> pd.DataFrame:#unwanted_cols: List) -> pd.DataFrame:
    data = pd.read_csv(path)
    #data.drop(unwanted_cols, axis=1, inplace=True)
    return data

@task
def get_classes(target_data: pd.Series) -> List[int]:
    return list(target_data.unique())

@task
def get_scaler(data: pd.DataFrame) -> Any:
    # scaling the numerical features
    scaler = StandardScaler()
    scaler.fit(data)

    return scaler

@task
def rescale_data(data: pd.DataFrame, scaler: Any) -> pd.DataFrame:
    # scaling the numerical features
    # column names are (annoyingly) lost after Scaling
    # (i.e. the dataframe is converted to a numpy ndarray)
    data_rescaled = pd.DataFrame(scaler.transform(data),
                                 columns=data.columns,
                                 index=data.index)
    return data_rescaled

@task
def label_encoder_fun() -> Any:
    label_encoder = preprocessing.LabelEncoder()
    return label_encoder

@task
def split_data(input_: pd.DataFrame, output_: pd.Series, test_data_ratio: float) -> Dict[str, Any]:
    X_tr, X_te, y_tr, y_te = train_test_split(input_, output_, test_size=test_data_ratio, random_state=0)
    return {'X_TRAIN': X_tr, 'Y_TRAIN': y_tr, 'X_TEST': X_te, 'Y_TEST': y_te}

@task
def find_best_model(X_train: pd.DataFrame, y_train: pd.Series, estimator: Any, parameters: List) -> Any:
    # Enabling automatic MLflow logging for scikit-learn runs
    mlflow.sklearn.autolog(max_tuning_runs=None)

    with mlflow.start_run():
        clf = GridSearchCV(
            estimator=estimator,
            param_grid=parameters,
            scoring='neg_mean_squared_error',
            cv=5,
            return_train_score=True,
            verbose=1
        )
        clf.fit(X_train, y_train)

        # Disabling autologging
        mlflow.sklearn.autolog(disable=True)

        return clf

# Workflow
@flow
def main(path: str='./data/diamonds.csv',target: str='price', test_size: float=0.2):
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("DiamondPrice_Experiment")

    # Define Parameters
    TARGET_COL = target
    #UNWANTED_COLS = ['Id']
    TEST_DATA_RATIO = test_size
    DATA_PATH = path

    # Load the Data
    dataframe = load_data(path=DATA_PATH)#, unwanted_cols=UNWANTED_COLS)

    # Identify Target Variable
    target_data = dataframe[TARGET_COL]
    input_data = dataframe.drop([TARGET_COL], axis=1)

    # Get Unique Classes
    classes = get_classes(target_data=target_data)

    # Split the Data into Train and Test
    train_test_dict = split_data(input_=input_data, output_=target_data, test_data_ratio=TEST_DATA_RATIO)
    # Rescaling Train and Test Data
    scaler = get_scaler(train_test_dict['X_TRAIN'].select_dtypes(include=['int64', 'float64']))
    num_train = rescale_data(data=train_test_dict['X_TRAIN'].select_dtypes(include=['int64', 'float64']), scaler=scaler)
    num_test = rescale_data(data=train_test_dict['X_TEST'].select_dtypes(include=['int64', 'float64']), scaler=scaler)

    num_train = pd.DataFrame(num_train)
    num_test = pd.DataFrame(num_test)

    #Label Encoding
    label_encoder = label_encoder_fun()
    cat_train =  train_test_dict['X_TRAIN'].select_dtypes(include=['object'])
    cat_train =  cat_train.apply(label_encoder.fit_transform)
    cat_train = pd.DataFrame(cat_train)

    cat_test = train_test_dict['X_TEST'].select_dtypes(include=['object'])
    cat_test = cat_test.apply(label_encoder.fit_transform)
    cat_test = pd.DataFrame(cat_test)

    X_train_transformed = pd.concat([num_train,cat_train], axis=1)
    X_test_transformed = pd.concat([num_test,cat_test], axis=1)


    # Model Training
    ESTIMATOR = KNeighborsRegressor()
    HYPERPARAMETERS = [{'n_neighbors': [i for i in range(1, 15)], 'p': [1,2]}]
    regressor = find_best_model(X_train_transformed,train_test_dict['Y_TRAIN'], ESTIMATOR, HYPERPARAMETERS)
    print(regressor.best_params_)


# Deploy the main function
from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta

deployment = Deployment.build_from_flow(
    flow=main,
    name="model_training",
    schedule=IntervalSchedule(interval=timedelta(hours=168)),
    work_queue_name="ml"
)
deployment.apply()