import streamlit as st
import pandas as pd
import numpy as np

mean = st.slider("Mean of x", 0,10)
name = st.text_input("Enter your name here:")
age = st.number_input("Enter your age here:")

st.write(f'Hello {name}. You are {age: .2f}')

df = pd.DataFrame({'x':np.random.normal(loc = mean, size = 100),
                   'y':np.random.normal(size = 100)})

st.title("My First App")

st.header("It shows some data")   

st.write("The slider equals", mean)

st.dataframe(df)