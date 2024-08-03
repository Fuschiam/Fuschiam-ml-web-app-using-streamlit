import streamlit as st
from pickle import load
import pandas as pd

model = load(open("best_model.pkl", "rb"))
class_dict = {
    "0": "age",
    "1": "bmi",
    "2": "children",
    "3": "sex_female",
    "4": "sex_male",
    "5": "smoker_no",
    "6": "smoker_yes",
    "7": "region_northeast",
    "8": "region_northwest",
    "9": "region_southeast",
    "10": "region_southwest"
}

st.title("Medical Cost - Model prediction")

val1 = st.slider("age", min_value = 0.0, max_value = None, step = 0.1)
val2 = st.slider("bmi", min_value = 0.0, max_value = 50, step = 0.1)
val3 = st.slider("children", min_value = 0.0, max_value = None, step = 0.1)
val4 = st.slider("sex_female", min_value = 0.0, max_value = 4.0, step = 0.1)
val5 = st.slider("sex_male", min_value = 0.0, max_value = 4.0, step = 0.1)
val6 = st.slider("smoker_no", min_value = 0.0, max_value = 4.0, step = 0.1)
val7 = st.slider("smoker_yes", min_value = 0.0, max_value = 4.0, step = 0.1)
val8 = st.slider("region_northeast", min_value = 0.0, max_value = 4.0, step = 0.1)
val9 = st.slider("region_northwest", min_value = 0.0, max_value = 4.0, step = 0.1)
val10 = st.slider("region_southeast", min_value = 0.0, max_value = 4.0, step = 0.1)
val11 = st.slider("region_southwest", min_value = 0.0, max_value = 4.0, step = 0.1)


if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)
   
