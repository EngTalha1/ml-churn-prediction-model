import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

st.title("Customer Churn Prediction App")

# =========================
# CUSTOMER INFO
# =========================
st.header("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    partner = st.selectbox("Partner", ["Yes", "No"])

with col2:
    senior = st.selectbox("Senior Citizen", [0, 1])
    dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.number_input("Tenure", 0, 100, value=12)

# =========================
# SERVICE INFO
# =========================
st.header("📡 Service Information")

col1, col2 = st.columns(2)

with col1:
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

with col2:
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

# =========================
# BILLING INFO
# =========================
st.header("💳 Billing Information")

col1, col2 = st.columns(2)

with col1:
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with col2:
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)

# =========================
# PREDICTION
# =========================
if st.button("Predict"):

    input_df = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    # encode categorical columns exactly like training
    cat_cols = input_df.select_dtypes(include="object").columns

    encoded = encoder.transform(input_df[cat_cols])

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(cat_cols)
    )

    numeric_df = input_df.drop(columns=cat_cols).reset_index(drop=True)

    final_input = pd.concat([numeric_df, encoded_df], axis=1)

    prediction = model.predict(final_input)

    if prediction[0] == 1:
        st.error("Customer will CHURN")
    else:
        st.success("Customer will STAY")