import streamlit as st
import pandas as pd
def app():
    st.title("Welcome to Pub Location Page")
    st.write("Display a Map.Based on the Postal Code or Local Authority, display all the pubs in the area chosen")
    df = pd.read_csv("Data/pubs_data.csv")
    df['postcode'] = df['postcode'].astype('string')
    df['latitude'] = df['latitude'].astype('float64')
    df['longitude'] = df['longitude'].astype('float64')
    postal_list =  df['postcode'].unique()
    postal_list =  list(postal_list)
    choosen = st.selectbox(
                'Choose a PostCode',
                postal_list
    )
    st.write('Choosen Postal_list',choosen)
    button_click = st.button("Display Pubs")
    if button_click == True:
        loc = df[df['postcode'] == choosen]
        lat = list(loc['latitude'])
        lon = list(loc['longitude'])
        df1 = pd.DataFrame({'lat': lat, 'lon':lon},dtype='float64')
        st.map(df1)