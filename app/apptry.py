import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

st.header(":sunglasses: :blue[Grace's _Try with the Streamlit_ ] :sunglasses:")

st.subheader("1. Your information")
name = st.text_input("Enter your name here👀")
age = st.number_input("How old are you?")
st.write(f'Hello {name}. You are {age} years old now.')

apps = ["Instagram","Twitter","Facebook","Snapchat","Wechat"]
st.subheader("2. Selectbox from a list")
apps_selected = st.selectbox("What is your favorate app?", options = apps)

time_on_social_media = ["0 hours", "1-2 hours", "3-5 hours", "More than 5 hours"]
average_time = st.selectbox("How long do you spend on social media everyday?", options = time_on_social_media)

st.button('SUBMIT')

with st.spinner("Wait for two seconds!..."):
    time.sleep(2)
st.success("Congrats!")
st.balloons()

st.subheader("Scatterplot on map")
df = pd.DataFrame(np.random.randn(1000,2)/[50,50]+[37.76,-122.4],columns = ['lat','lon'])
st.map(df)

from bokeh.plotting import figure
x = [1,3,5]
y = [2,7,3]
simple_line = figure(title = 'an example with line chart', x_axis_label = 'x', y_axis_label = 'y')
simple_line.line(x,y,legend_label = 'Analysis', line_width = 2)
st.bokeh_chart(simple_line, use_container_width = True)

st.header("Diabetes Prediction")

from PIL import Image
image = Image.open("diabetes.jpg")
st.image(image, caption = 'diabetes')

with open ('diabetes_model.pkl','rb') as f:
    model = pickle.load(f)
Pregnancies = st.number_input("Pregnancies")
Glucose = st.number_input("Glucose")
BloodPressure = st.number_input("Blood Pressure")
SkinThickness = st.number_input("Skin Thickness")
Insulin = st.number_input("Insulin")
BMI = st.number_input("BMI")
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function")
Age = st.number_input("Age")
X = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
prediction = model.predict(X)
st.button('MAKE PREDICTION')
st.write("Your result is ", prediction[0])

if prediction == 0:
    st.write(":green[Not diagnosed]")
else:
    st.write(":red[Diagnosed]")