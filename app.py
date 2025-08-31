import streamlit as st
import joblib
import pandas as pd

st.title("🚗 Advanced Car Price Predictor")

# Simple inputs
year = st.number_input("Manufacturing Year", 2000, 2025, 2015)
kms = st.number_input("Kilometers Driven", 0, 500000, 50000)

# New inputs for fuel type and brand
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
brand = st.selectbox("Brand", ["Maruti", "Hyundai", "Honda", "Toyota", "Ford", "Tata", "Mahindra"])

if st.button("Predict"):
    try:
        # Load model directly (no dictionary)
        model = joblib.load("car_price_model.joblib")
        
        # Create a DataFrame with all features (including the new ones)
        # Note: You'll need to retrain your model with these additional features
        input_data = pd.DataFrame({
            'year': [year],
            'kms_driven': [kms],
            'fuel_type': [fuel_type],
            'brand': [brand]
        })
        
        # Predict with all features
        price = model.predict(input_data)[0]
        st.success(f"Estimated Price: ₹{price:,.0f}")
        
    except Exception as e:
        st.error(f"Oops! {str(e)}")
