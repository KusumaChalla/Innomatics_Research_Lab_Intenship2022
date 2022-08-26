import streamlit as st
import pandas as pd
import numpy as np
def app():
    st.title("Welcome to Find the Nearest Pub Page")
    st.write("User to enter his/her Latitude and Longitude. Display the nearest 5 Pubs on the map. Use Euclidean Distance to find the nearest pubs")
    df = pd.read_csv("Data/pubs_data.csv")
    df['latitude'] = df['latitude'].astype('float64')
    df['longitude'] = df['longitude'].astype('float64')
    lat = st.number_input('Enter latitude',format="%.6f")
    lon = st.number_input('Enter longitude',format="%.6f")

    button_click = st.button("Display Pubs")
    if button_click == True:
        if lat != 0.00 and lon!= 0.00:
            ############logic#####################
            arr_lat = np.array(df['latitude'])
            arr_lon = np.array(df['longitude'])
            arr = np.vstack((arr_lat, arr_lon)).T
            ar = np.sqrt(np.sum((arr - (lat, lon)) ** 2, axis=1))
            ar = ar.reshape(-1, 1)
            res = np.hstack([arr, ar])
            d = pd.DataFrame(res, columns=['lat', 'lon', 'dict'])
            k = np.sort(res[:, [2]].ravel())[1:6]
            l = list(k)
            lat1 = []
            lon1 = []
            for i in l:
                f = d.loc[d['dict'] == i]
                lat1.append(float(f['lat'].values))
                lon1.append(float(f['lon'].values))

            df1 = pd.DataFrame({'lat': lat1, 'lon': lon1}, dtype='float64')
            st.map(df1)

        else:
            st.write("Enter lat,lon values again")
