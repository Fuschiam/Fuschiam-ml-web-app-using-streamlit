#url to render https://fuschiam-ml-web-app-using-streamlit.onrender.com

import streamlit as st
import pickle
from pickle import load
import pandas as pd

# Load the model
model = load(open("sl_model.pkl", "rb"))

# Inject custom CSS with a new color
st.markdown("""
    <style>
    /* Styling the sliders */
    .streamlit-expanderHeader {
        font-family: 'Arial', sans-serif;
        color: #4A90E2; /* Custom blue color */
    }
    .stSlider {
        color: #7ED321; /* Custom green color */
    }
    .stSlider div[role="slider"] {
        background: #c50cd3; /* Custom red color */
        border-radius: 10px;
    }
    .stSlider input[type="range"]::-webkit-slider-thumb {
        background: #c50cd3; /* Custom red color */
        border-radius: 10px;
        height: 20px;
        width: 20px;
    }
    .stSlider input[type="range"]::-moz-range-thumb {
        background: #c50cd3; /* Custom red color */
        border-radius: 10px;
        height: 20px;
        width: 20px;
    }
    .stSlider input[type="range"]::-ms-thumb {
        background: #c50cd3; /* Custom red color */
        border-radius: 10px;
        height: 20px;
        width: 20px;
    }
    .stSlider {
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the app with custom style
st.markdown('<h1 style="font-family: Arial, sans-serif; color: #4A90E2; text-align: center;">Medical Cost - Model Prediction</h1>', unsafe_allow_html=True)

# Create sliders with default Streamlit styling but customized with CSS
val1 = st.slider("Age", min_value=0, max_value=100, step=1, key="age_slider")
val2 = st.slider("BMI", min_value=0, max_value=50, step=1, key="bmi_slider")
val3 = st.slider("Children", min_value=0, max_value=20, step=1, key="children_slider")

# Radio button for sex selection
sex = st.radio("Sex", options=["Female", "Male"], key="sex_radio")
val4 = 1 if sex == "Female" else 0
val5 = 1 if sex == "Male" else 0

# Radio button for smoker status
smoker = st.radio("Smoker", options=["Yes", "No"], key="smoker_radio")
val6 = 1 if smoker == "No" else 0
val7 = 1 if smoker == "Yes" else 0

# Radio button for region selection
region = st.radio("Region", options=[
    "Northeast", "Northwest", "Southeast", "Southwest"], key="region_radio")
val8 = 1 if region == "Northeast" else 0
val9 = 1 if region == "Northwest" else 0
val10 = 1 if region == "Southeast" else 0
val11 = 1 if region == "Southwest" else 0

if st.button("Predict"):
    new_data_point_dict = {
        'age': [val1],
        'bmi': [val2],
        'children': [val3],
        'sex_female': [val4],
        'sex_male': [val5],
        'smoker_no': [val6],
        'smoker_yes': [val7],
        'region_northeast': [val8],
        'region_northwest': [val9],
        'region_southeast': [val10],
        'region_southwest': [val11],
    }

    # Convert the dictionary to a DataFrame
    new_data_point_df = pd.DataFrame(new_data_point_dict)

    # Make prediction
    pred_class = model.predict(new_data_point_df)[0]
    st.markdown(f'<p style="font-family: Arial, sans-serif; color: #FF5722; font-size: 24px; font-weight: bold;">Prediction: {pred_class}</p>', unsafe_allow_html=True)

# Create columns
col1, col2 = st.columns(2)

# Display images in columns
with col1:
    st.image("/workspaces/Fuschiam-ml-web-app-using-streamlit/data/raw/irwan-rbDE93-0hHs-unsplash.jpg", use_column_width=True)
with col2:
    st.image("/workspaces/Fuschiam-ml-web-app-using-streamlit/data/raw/kenny-eliason-5ddH9Y2accI-unsplash.jpg", use_column_width=True)