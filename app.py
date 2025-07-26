import streamlit as st
import joblib
import pandas as pd

st.title("🚗 Basic Car Price Predictor")

# Simple inputs
year = st.number_input("Manufacturing Year", 2000, 2025, 2015)
kms = st.number_input("Kilometers Driven", 0, 500000, 50000)

if st.button("Predict"):
    try:
        # Load model directly (no dictionary)
        model = joblib.load("car_price_model.joblib")
        
        # Predict with just year and kms
        price = model.predict([[2025-year, kms]])[0]
        st.success(f"Estimated Price: ₹{price:,.0f}")
        
    except Exception as e:
        st.error(f"Oops! {str(e)}")
