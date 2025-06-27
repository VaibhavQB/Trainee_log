import streamlit as st  # type: ignore
import numpy as np
import pandas as pd
import tensorflow as tf     # type: ignore
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder     # type: ignore
import pickle
from tensorflow.keras.models import load_model   # type: ignore


# Load Model

model = load_model('classification_model.h5')


# Load the encoders and scaler

with open('onehot_encoder_geo.pkl', 'rb') as f:
    geo_encoder = pickle.load(f)

with open('label_encoder_gender.pkl', 'rb') as f :
    gender_encoder = pickle.load(f)

with open('scaler.pkl', 'rb') as f :
    scaler = pickle.load(f)


# Streamlit App

st.title('Customer Rukega ki nahi?? Jaanlo.')


# User Inputs

geo = st.selectbox('Geography', geo_encoder.categories_[0])
gender = st.selectbox('Gender', gender_encoder.classes_)
age = st.slider('Age', 17, 117)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
est_sal = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 7, 1)
nop = st.slider('Number of Products', 1, 4)
has_cc = st.selectbox('Has Credit Card', [0, 1])
is_active = st.selectbox('Is Active Member', [0, 1])


# Preparing the input data for the model

input_data_df = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [gender_encoder.transform([gender])][0],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [nop],
    'HasCrCard': [has_cc],
    'IsActiveMember': [is_active],
    'EstimatedSalary': [est_sal]
})


# For Geography we'll use encoder

geo_encoded = geo_encoder.transform([[geo]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=geo_encoder.get_feature_names_out(['Geography']))


# Combine New Geography columns with input data


input_df = pd.concat([input_data_df.reset_index(drop=True), geo_encoded_df], axis=1)


# Scaling Input DF

input_data_scaled = scaler.transform(input_df)

# Time to Predict

prediction = model.predict(input_data_scaled)
prediction_bab = prediction[0][0]

# Showin it on StreamLit app



if prediction_bab > 0.5 :
    st.write("Yeah nahi rukega, kyu??")
    st.write("Yeah raaz bhi ussi ke saath chala gaya")
    st.write(f'Dekh lo Model Prediction = {prediction[0][0]:.2f}')
else:
    st.write("Rukega Yeah!!")
    st.write("Mai bol raha hu na rukega yeah.")
    st.write(f'Dekho Model Prediction = {prediction[0][0]:.2f}')

