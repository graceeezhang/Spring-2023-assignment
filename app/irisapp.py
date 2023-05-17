import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.header('Preedicting Flowers')

with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

sepal_width = st.number_input('Sepal width')
sepal_kength = st.number_input('Sepal length')
petal_width = st.number_input('Petal width')
petal_length = st.number_input('Petal length')

X = np.array([[sepal_width, sepal_kength, petal_width, petal_length]])

prediction = model.predict(X)

st.write("Your flower is a", prediction[0])