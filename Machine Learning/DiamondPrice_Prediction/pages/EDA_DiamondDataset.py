import streamlit as st
import pandas as pd
import io
from PIL import Image
def app():
    st.title("Exploratory Data Analysis on Diamond Dataset")
    df = pd.read_csv("Data/diamonds.csv")
    st.subheader('Dataframe:')
    n, m = df.shape
    st.write(f'<p style="font-size:130%">Dataset contains {n} rows and {m} columns.</p>', unsafe_allow_html=True)
    st.dataframe(df)

    all_vizuals = ['Info', 'NA Info', 'Descriptive Analysis',
                   'Distribution of Numerical Columns', 'Count Plots of Categorical Columns',
                   'HeapMap of numeric features']

    vizuals = st.sidebar.multiselect("Choose which visualizations you want to see ", all_vizuals)

    if 'Info' in vizuals:
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()

        st.text(s)

    if 'NA Info' in vizuals:
        st.subheader('NA Value Information:')
        if df.isnull().sum().sum() == 0:
            st.write('There is no NA value in the dataset.')
        else:
            st.write(df.isnull().sum())

    if 'Descriptive Analysis' in vizuals:
        st.subheader('Descriptive Analysis:')
        st.dataframe(df.describe())

    if 'Distribution of Numerical Columns' in vizuals:
        numer = ['carat','depth','table','x','y','z']
        choice = st.selectbox("Choose which visualizations you want to see ", numer)
        if choice in numer:
            if choice == 'carat':
                image = Image.open('images/carat.jpg')
                st.image(image)
            if choice == 'depth':
                image = Image.open('images/depth.jpg')
                st.image(image)
            if choice == 'table':
                 image = Image.open('images/table.jpg')
                 st.image(image)
            if choice == 'x':
                image = Image.open('images/x.jpg')
                st.image(image)
            if choice == 'y':
                image = Image.open('images/y.jpg')
                st.image(image)
            if choice == 'z':
                image = Image.open('images/z.jpg')
                st.image(image)
        else:
            st.write('choose again')

    if 'Count Plots of Categorical Columns' in vizuals:
        cato = ['cut','color','clarity']
        choice = st.selectbox("Choose which visualizations you want to see 👇", cato)
        if choice in cato:
            if choice == 'cut':
                image = Image.open('images/cut.jpg')
                st.image(image)
            if choice == 'color':
                image = Image.open('images/color.jpg')
                st.image(image)
            if choice == 'clarity':
                image = Image.open('images/clarity.jpg')
                st.image(image)
        else:
            st.write('choose again')

    if 'HeapMap of numeric features' in vizuals:
        image = Image.open('images/heatmap.jpg')
        st.image(image)




