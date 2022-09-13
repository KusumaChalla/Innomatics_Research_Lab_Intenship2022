import streamlit as st
import pandas as pd
import numpy as np
from pickle import load

def app():
    st.title("Welcome to Predict_DiamondPrice Page")
    st.subheader("Enter the Diamond Properties below to predict the price")
    df = pd.read_csv("Data/diamonds.csv")

    carat = st.slider('Carat',min_value=0.10, max_value=5.00)

    df['cut'] = df['cut'].astype('string')
    cut_list = df['cut'].unique()
    cut_v = st.selectbox(
        'cut',
        cut_list
    )

    df['color'] = df['color'].astype('string')
    color_list = df['color'].unique()
    color_v = st.selectbox(
        "color",
        color_list
    )

    df['clarity']= df['clarity'].astype('string')
    clarity_list = df['clarity'].unique()
    clarity_v = st.selectbox(
        "clarity",
        clarity_list
    )

    cut_encoder = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Ideal': 4, 'Premium': 5}
    cut = cut_encoder.get(cut_v)

    color_encoder = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
    color = color_encoder.get(color_v)

    clarity_encoder = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}
    clarity = clarity_encoder.get(clarity_v)

    depth = st.slider('Depth(per table)',min_value=10.00, max_value=100.00,step=0.01)
    table = st.slider('table',min_value=10.00, max_value=100.00,step=0.01)
    x = st.slider('X(length)',min_value=1.00, max_value=15.00,step = 0.01)
    y = st.slider('Y(width)',min_value=1.00, max_value=30.00,step=0.01)
    z = st.slider('Z(depth)',min_value=1.00, max_value=30.00,step=0.01)

    scaler = load(open("Data/Models/standard_scaler.pkl", 'rb'))
    rfm  = load(open("Data/Models/RF_model.pkl",'rb'))


    button_click = st.button("GET DIAMOND_PRICE")
    if button_click == True:
        if carat and cut and color_v and clarity_v and depth and table and x and y and z:
            num_ = np.array([float(carat),float(depth),float(table),x,y,z]).reshape(1,-1)
            num_ = scaler.transform(num_)
            query = np.append(num_,[cut,color,clarity]).reshape(1,-1)
            pred = rfm.predict(query)
            st.success(pred)
            st.write("Confidence interval for predicted diamond price :  -272 to +272 ")
            st.write("Predicted diamond price in dollors",str(pred))
        else:
            st.error("ENTER VALUES AGAIN")





