import streamlit as st
import base64
from multipage import MultiPage
from pages import About_Diamonds,EDA_DiamondDataset,Predict_DiamondPrice

app1 = MultiPage()


new_title = '<p style="font-family:sans-serif; color:blue; font-size: 42px;">Diamond Price Prediction Application </p>'
st.markdown(new_title, unsafe_allow_html=True)

app1.add_page("HomePage", About_Diamonds.app)
app1.add_page("Exploratory Data Analysis", EDA_DiamondDataset.app)
app1.add_page("Diamond Price Prediction", Predict_DiamondPrice.app)

app1.run()