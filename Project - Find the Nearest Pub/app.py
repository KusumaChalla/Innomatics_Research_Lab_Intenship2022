import streamlit as st
from multipage import MultiPage
from pages import HomePage,PubLocations,FindtheNearestPub

app1 = MultiPage()

st.markdown(""" 
# Open Pub Application 
""")

app1.add_page("Home Page", HomePage.app)
app1.add_page("Pub Locations", PubLocations.app)
app1.add_page("Find the nearest Pub", FindtheNearestPub.app)

app1.run()

