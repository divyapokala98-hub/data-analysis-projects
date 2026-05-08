import pandas as pd
import streamlit as st
import joblib
import numpy as np

model = joblib.load("F:\\Divya\\Project 2\\final_model.pkl")
scaler = joblib.load("F:\\Divya\\Project 2\\scaler.pkl")
expected_columns = joblib.load("F:\\Divya\\Project 2\\columns.pkl")


st.title("🍹🔎 BEVERAGE PREDICTION")
st.header("📝 Provide The Following Details")


Beverage_category = st.selectbox('Beverage_category',
                                 [
                                 'Classic Espresso Drinks',
                                 'Coffee',
                                 'Frappuccino® Blended Coffee',
                                 'Frappuccino® Blended Crème',
                                 'Frappuccino® Light Blended Coffee',
                                  'Shaken Iced Beverages',
                                  'Signature Espresso Drinks',
                                 'Smoothies',
                                  'Tazo® Tea Drinks'])
Beverage_prep = st.selectbox('Beverage_prep',
                             [
                              '2% Milk', 
                              'Doppio', 
                              'Grande',
                              'Grande Nonfat Milk', 
                              'Short',
                              'Short Nonfat Milk',
                              'Soymilk',
                              'Tall', 
                              'Tall Nonfat Milk',
                              'Venti', 
                              'Venti Nonfat Milk',
                              'Whole Milk'])
Calories = st.number_input('Calories',0,500,350)
Total_Fat_g = st.number_input(' Total Fat (g)',0,40,25)
Trans_Fat_g = st.number_input('Trans Fat (g) ',0,10,5)
Saturated_Fat_g = st.number_input('Saturated Fat (g)',0.0,0.5,0.2)
Sodium_mg = st.number_input(' Sodium (mg)',0,50,25)
Total_Carbohydrates_g = st.number_input(' Total Carbohydrates (g) ',0,400,250)
Cholesterol_mg = st.number_input('Cholesterol (mg)',0,100,65)
Dietary_Fibre_g = st.number_input(' Dietary Fibre (g)',0,10,5)
Sugar_g = st.number_input(' Sugars (g)',0,100,60)
Protein_g = st.number_input(' Protein (g) ',0,30,15)
Vitamin_A_DV = st.number_input('Vitamin A (% DV) ',0,60,45)
Vitamin_C_DV = st.number_input('Vitamin C (% DV)',0,100,80)
Calcium_DV =st.number_input(' Calcium (% DV) ',0,70,55)
Iron_DV = st.number_input('Iron (% DV) ',0,60,45)
Caffeine_mg = st.number_input('Caffeine (mg)',0,300,250)


if st.button('PREDICT'):
    raw_input = {
        'Beverage_category' : Beverage_category,
        'Beverage_prep'   : Beverage_prep,
        'Calories' : Calories, 
        ' Total Fat (g)': Total_Fat_g ,
        'Trans Fat (g) ' :Trans_Fat_g ,
        'Saturated Fat (g)' :Saturated_Fat_g,
        ' Sodium (mg)' : Sodium_mg ,
        ' Total Carbohydrates (g) ' : Total_Carbohydrates_g ,
        'Cholesterol (mg)' :Cholesterol_mg,
        ' Dietary Fibre (g)' :Dietary_Fibre_g,
        ' Sugars (g)' :Sugar_g ,
        ' Protein (g) ' :Protein_g ,
        'Vitamin A (% DV) ' : Vitamin_A_DV,
        'Vitamin C (% DV)' : Vitamin_C_DV,
        ' Calcium (% DV) ' : Calcium_DV,
        'Iron (% DV) ' : Iron_DV,
        'Caffeine (mg)' : Caffeine_mg,
    } 

    input_df = pd.DataFrame([raw_input])
    input_df = pd.get_dummies(input_df,columns=["Beverage_category","Beverage_prep"],dtype=int)
    input_df = input_df.reindex(columns = expected_columns,fill_value=0)
    input_df_scaled = scaler.transform(input_df)
    prediction =model.predict(input_df_scaled)

    st.success(f"YOUR BEVERAGE DRINK IS :-🍹 **{prediction[0]}**")