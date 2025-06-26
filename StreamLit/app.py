import streamlit as st  # type: ignore
import numpy as np
import pandas as pd

# Title of the Application
st.title("This is a practice")

# Display a simple text 
st.write("This is as it is")

# Creat a Simple data frame

df = pd.DataFrame({
    'First Column' : list(range(10)),
    'Second Column' : list(range(10,20)) 
})

# Display the DataFrame
st.write('Here is the Data Frame')
st.write(df)

# Create a line Chart

chart_data  = pd.DataFrame(
    np.random.randn(20,3), columns=['x','y','z']
)
st.line_chart(chart_data)


