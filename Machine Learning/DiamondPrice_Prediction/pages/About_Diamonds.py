import streamlit as st
from PIL import Image
def app():
    st.title("Welcome to Home Page")

    image = Image.open('images/sc4.jpg')
    st.image(image)
    image = Image.open('images/sc9.jpg')
    st.image(image)
    image = Image.open('images/sc5.jpg')
    st.image(image)
    image = Image.open('images/sc6.jpg')
    st.image(image)
    image = Image.open('images/sc7.jpg')
    st.image(image)
    image = Image.open('images/sc8.jpg')
    st.image(image)
    image1 = Image.open('images/sc2.jpg')
    st.write("Diamond Properties")
    st.image(image1)
    image2 = Image.open('images/sc3.jpg')
    st.write("Example of applications")
    st.image(image2)