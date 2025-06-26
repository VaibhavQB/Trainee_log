import streamlit as st  # type: ignore
import pandas as pd 
import numpy as np

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Selecte you age: ", 0, 125, 15)

options = ['Pyhton', 'Java', 'C++', "JavaScript"]
choice = st.selectbox('Choose your language: ',options)
st.write(f'You Selected {choice}.')

if name :
    st.write(f"Hello, {name}")

uploaded = st.file_uploader("Upload a CSV File: ", type='csv')

if uploaded is not None :
    df = pd.read_csv(uploaded)
    st.write(df)