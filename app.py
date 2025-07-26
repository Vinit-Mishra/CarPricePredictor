# Remove the manual joblib install attempt (not needed)
import streamlit as st
import pandas as pd
import joblib
import os

st.title("🚗 Car Price Predictor")

model_path = "car_price_model.joblib"
if os.path.exists(model_path):
    try:
        # Load model (now expecting a dictionary with model and preprocessor)
        loaded = joblib.load(model_path)
        model = loaded['model']
        preprocessor = loaded['preprocessor']
        
        col1, col2 = st.columns(2)
        
        # New inputs
        company = col1.selectbox("Company", 
                               ["Maruti", "Hyundai", "Mahindra", "Tata", 
                                "Honda", "Toyota", "Ford", "Chevrolet"])
        fuel_type = col2.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
        
        # Existing inputs
        year = col1.number_input("Year of Manufacture", 
                               min_value=1990, max_value=2025, value=2015)
        kms = col2.number_input("KMs Driven", 
                              min_value=0, max_value=500000, value=40000)

        if st.button("Predict Price"):
            # Prepare input with ALL features
            input_dict = {
                'company': [company],
                'fuel_type': [fuel_type],
                'year': [year],
                'kms_driven': [kms]
            }
            input_df = pd.DataFrame(input_dict)
            
            # Create 'age' feature
            input_df['age'] = 2025 - input_df['year']
            
            # Preprocess and predict
            X_processed = preprocessor.transform(input_df)
            price = model.predict(X_processed)[0]
            st.success(f"Estimated Price: ₹{price:,.0f}")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.error("🚫 Model file not found or invalid! Please check:")
    st.write("- File exists in same directory")
    st.write("- Contains both model and preprocessor")
