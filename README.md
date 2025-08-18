# 🚗 Car Price Predictor

A simple **Streamlit web app** that predicts the resale price of a car
based on its **manufacturing year** and **kilometers driven**.\
This project uses a pre-trained machine learning model (`scikit-learn`)
saved as `car_price_model.joblib`.

------------------------------------------------------------------------

## ✨ Features

-   User-friendly interface built with **Streamlit**\
-   Predicts car price instantly\
-   Inputs:
    -   Manufacturing Year\
    -   Kilometers Driven

------------------------------------------------------------------------

## 📦 Installation

1.  **Clone this repository** (or download the files):

    ``` bash
    git clone https://github.com/yourusername/car-price-predictor.git
    cd car-price-predictor
    ```

2.  **Create a virtual environment** (recommended):

    ``` bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```

3.  **Install dependencies**:

    ``` bash
    pip install -r requirements.txt
    ```

------------------------------------------------------------------------

## 🚀 Usage

Run the Streamlit app:

``` bash
streamlit run app.py
```

Then open your browser at:

    http://localhost:8501

------------------------------------------------------------------------

## 📁 Project Structure

    .
    ├── app.py                 # Streamlit app
    ├── car_price_model.joblib # Trained ML model
    ├── requirements.txt       # Project dependencies
    └── README.md              # Project documentation

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Python**\
-   **Streamlit** -- Web UI\
-   **scikit-learn** -- Machine Learning\
-   **pandas / numpy** -- Data handling\
-   **joblib** -- Model serialization

------------------------------------------------------------------------

## 🧑‍💻 Example

-   Input:
    -   Year: `2015`\
    -   Kms Driven: `50,000`\
-   Output:
    -   `Estimated Price: ₹3,45,000`

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Add more input features (fuel type, brand, transmission, etc.)\
-   Deploy on **Streamlit Cloud**, **Heroku**, or **AWS**\
-   Improve model accuracy with advanced algorithms
