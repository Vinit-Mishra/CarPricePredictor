
# Ensure joblib is installed even if requirements.txt fails
try:
    import joblib
except ImportError:

    import joblib

import streamlit as st
import pandas as pd
import numpy as np
import os

st.title("🚗 Car Price Predictor")

model_path = "car_price_model.joblib"
if os.path.exists(model_path):
    model = joblib.load(model_path)

    col1, col2 = st.columns(2)
    year = col1.number_input("Year of Manufacture", min_value=1990, max_value=2025, value=2015)
    kms = col2.number_input("KMs Driven", min_value=0, max_value=500000, value=40000)

    if st.button("Predict Price"):
        age = 2025 - year
        input_df = pd.DataFrame([[age, kms]], columns=["age", "kms_driven"])
        price = model.predict(input_df)[0]
        st.success(f"Estimated Price: ₹ {price:,.0f}")
else:
    st.error("🚫 Model file not found! Please upload `car_price_model.joblib` to this repo.")
