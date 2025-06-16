import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title='Medical Insurance Cost Predictor',layout='centered')
st.title('Medical Insurance Cost Prediction system')
st.markdown('''** Welcome our valued Client !!!
 This is the cost prediction system of the Medical Insurance which Tries to Predict cost from the below asked Features .
 Fill All the Features Properly. ** ''')

st.markdown('---')

def load_model():
 with open('linearmodel.pkl','rb') as f:
  return pickle.load(f)

model = load_model()
col1,col2 = st.columns(2)
with col1:
 Age = st.number_input("Enter The Person's Age : ",min_value=0,max_value=110)
 Gender = st.select_box("What is the Person's gender : ",["Male","Female"])
 BMI = st.number_input("Enter the body Mass Index of the Person : ",min_value=0.0, max_value=45.0)

with col2:
 Nchildrens = st.select_box("No. of childrens person have : ",['0','1','2','3+'])
 smoker = st.select_box("does he/she smoke ? : ",['smoker','non smoker'])
 region = st.select_box("Which Reason does he/she belongs to ? ",['Northeast','Northwest','Southeast','Southwest'])

gender_map = {'Male':1,'Female':0}
child_map = {'0':0,'1':1,'2':2,'3+':3}
smoker_map = {'non smoker':0,'smoker':1}
region_map = {'Northeast':0,'Northwest':1,'Southeast':2,'Southwest':3}

if st.button("Predict the Cost Price ->") : 
 features = [Age,gender_map[Gender],BMI,child_map[Nchildrens],smoker_map[smoker],region_map[region]]
 prediction = model.predict([features])
 st.sucess('The Cost Price of the Patients Medical insurance is Predicted to be arround Usd ',prediction[0])
 st.balloons()
