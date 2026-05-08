import joblib
import pandas as pd
import streamlit as st

model = joblib.load("F:\\Divya\\project 1\\Knn_model.pkl")
scaler = joblib.load("F:\\Divya\\project 1\\scaler.pkl")
expected_columns = joblib.load("F:\\Divya\\project 1\\columns.pkl")
encoders = joblib.load("F:\\Divya\\project 1\\label_encoders.pkl")

st.title("SLEEP APNEA AND INSOMNIA PREDICTION")
st.header("Provide the Following Details")

Age = st.slider("Age",18,100,25)
Gender = st.selectbox("Gender",["Male","Female"])
Occupation = st.selectbox("Occupation",["Teacher","Nurse","Doctor","Engineer","Manager","Sales Representative","Software Engineer","Lawyer","Accountant","Scientist"])
Sleep_Duration = st.number_input("Sleep_Duration",2.5,15.5,8.5)
Quality_of_Sleep = st.number_input("Quality_of_Sleep",2,15,6)
Physical_Activity_Level = st.number_input("Physical_Activity_Level",20,100,30)
Stress_Level = st.number_input("Stress_Level",2,10,5)
BMI_Category = st.selectbox("BMI_Category",["Normal","Overweight","Obese","Normalweight"])
Heart_Rate = st.number_input("Heart_Rate",50,100,75)
Daily_Steps = st.number_input("Daily_Steps",1000,50000,8000)
Systolic = st.number_input("Systolic",60,200,120)
Diastolic = st.number_input("Diastolic",60,200,120)

if st.button("predict"):
    raw_input = {
        "Age":Age,
       "Gender":Gender,
       "Occupation":Occupation,
       "Sleep Duration":Sleep_Duration,
       "Quality of Sleep":Quality_of_Sleep,
       "Physical Activity Level":Physical_Activity_Level,
       "Stress Level":Stress_Level,
       "BMI Category":BMI_Category,
       "Heart Rate":Heart_Rate,
       "Daily Steps":Daily_Steps,
       "Systolic":Systolic,
       "Diastolic":Diastolic
    }
   
    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in expected_columns:
            input_df[col]=0

    input_df =input_df[expected_columns]

    for col in ["Gender","Occupation","BMI Category"]:
        input_df[col] = encoders[col].transform(input_df[col].astype(str))


    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]


    if prediction == 1:
        st.error("SLEEP APNEA DETECTED")
    else:
        st.error("INSOMNIA DETECTED")