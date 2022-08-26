import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("Welcome to Home Page")
    st.write("Basic information and statistics about the dataset.")
    df = pd.read_csv("Data/pubs_data.csv")
    st.subheader("Pub_data")
    st.write(df.head())
    df['name'] = df['name'].astype('string')
    df['address'] = df['address'].astype('string')
    df['postcode'] = df['postcode'].astype('string')
    df['local_authority'] = df['local_authority'].astype('string')
    authority_count =  df['local_authority'].unique()
    pubs_count = df['name'].unique()
    st.subheader("Total No of Pubs")
    st.write(len(pubs_count))
    st.subheader("Total No of local_authority")
    st.write(len(authority_count))
    fig,ax = plt.subplots()
    sns.countplot(x='local_authority',data=df[0:200],ax=ax)
    ax.set_title("Some of the local_authority")
    st.pyplot(fig)





