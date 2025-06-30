# importing the required libraries
import numpy as np
import tensorflow as tf  # type: ignore
from tensorflow.keras.datasets import imdb   # type: ignore
from tensorflow.keras.preprocessing import sequence   # type: ignore
from tensorflow.keras.models import load_model   # type: ignore
import streamlit as st    # type: ignore



# Loading the Dataset
word_index = imdb.get_word_index()
reverse_word_index = {value : key for key, value in word_index.items()}


# Loading the pre-trained model
model = load_model('simple_rnn_imdb.keras')


# Helper Functions

# Func to Decode
def decode_review(encoded_reviews):
    return ' '.join([reverse_word_index.get(i-3, '?') for i in encoded_reviews])

# Func to Perprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review =[word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review


# Prediction Function
def predict_sentiment(review):
    preprocess_input = preprocess_text(review)

    prediction = model.predict(preprocess_input)

    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

    return sentiment, prediction[0][0]


# Stream-Lit App

st.title("Hit ya Flop: The Movie Review")
st.write("Batao batao kaisi lagi movie.")

# User Input
user_input = st.text_area('Movie Reviw')


if st.button("classify!!!") :

    # preprocess_input = preprocess_text(user_input)

    # Make Prediction
    sentiment, score = predict_sentiment(user_input)

    # Display the result
    st.write(f'Sentiment : {sentiment}')
    st.write(f'Prediction Score : {score}')
else:
    st.write('Please enter a review!!!')
