import streamlit as st
import numpy as np
import pickle

# Page configuration
st.set_page_config(page_title='Medical Insurance Cost Predictor', layout='centered')
st.title('💼 Medical Insurance Cost Prediction System')

# Description
st.markdown('''
**Welcome, our valued Client!**

This is a medical insurance cost prediction system that tries to predict the cost based on the features you provide below.  
Please fill in all the fields accurately.
''')
st.markdown('---')

# Load the model
def load_model():
    with open('linearmodel.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# Input fields
col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Enter the person's age:", min_value=0, max_value=110)
    Gender = st.selectbox("What is the person's gender:", ["Male", "Female"])
    BMI = st.number_input("Enter the body mass index (BMI):", min_value=0.0, max_value=45.0)

with col2:
    Nchildrens = st.selectbox("Number of children:", ['0', '1', '2', '3+'])
    smoker = st.selectbox("Does the person smoke?", ['non smoker', 'smoker'])
    region = st.selectbox("Which region do they belong to?", ['Northeast', 'Northwest', 'Southeast', 'Southwest'])

# Encoding categorical variables
gender_map = {'Male': 1, 'Female': 0}
child_map = {'0': 0, '1': 1, '2': 2, '3+': 3}
smoker_map = {'non smoker': 0, 'smoker': 1}
region_map = {'Northeast': 0, 'Northwest': 1, 'Southeast': 2, 'Southwest': 3}

# Prediction
if st.button("Predict the Insurance Cost →"):
    features = [
        Age,
        gender_map[Gender],
        BMI,
        child_map[Nchildrens],
        smoker_map[smoker],
        region_map[region]
    ]
    
    prediction = model.predict([features])
    st.success(f"The predicted cost of medical insurance is around **USD {prediction[0]:,.2f}**.")
    st.balloons()
