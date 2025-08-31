import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("🚗 Advanced Car Price Predictor")

# Simple inputs
year = st.number_input("Manufacturing Year", 2000, 2025, 2015)
kms = st.number_input("Kilometers Driven", 0, 500000, 50000)

# New inputs for fuel type and brand
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
brand = st.selectbox("Brand", ["Maruti", "Hyundai", "Honda", "Toyota", "Ford", "Tata", "Mahindra"])

if st.button("Predict"):
    try:
        # Load model
        model = joblib.load("car_price_model.joblib")
        
        # Calculate age (current year - manufacturing year)
        current_year = 2023  # You can update this annually or use datetime
        age = current_year - year
        
        # Create a DataFrame with the expected feature names
        # Note: This assumes your original model was trained with 'age' and 'kms_driven'
        input_data = pd.DataFrame({
            'age': [age],
            'kms_driven': [kms]
        })
        
        # If your model was trained with additional features, you need to add them here
        # For now, we'll use the original features only
        
        # Predict with the expected features
        price = model.predict(input_data)[0]
        st.success(f"Estimated Price: ₹{price:,.0f}")
        
    except Exception as e:
        st.error(f"Oops! {str(e)}")
