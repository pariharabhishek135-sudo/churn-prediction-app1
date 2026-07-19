import streamlit as st
import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Customer Churn Prediction")

CreditScore = st.number_input("Credit Score", 300, 900, 600)
Age = st.number_input("Age", 18, 100, 30)
Tenure = st.number_input("Tenure", 0, 10, 5)
Balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
NumOfProducts = st.number_input("Number of Products", 1, 4, 1)
HasCrCard = st.selectbox("Has Credit Card", [0, 1])
IsActiveMember = st.selectbox("Is Active Member", [0, 1])
EstimatedSalary = st.number_input("Estimated Salary", 0.0, 300000.0, 50000.0)

if st.button("Predict"):
    data = pd.DataFrame([[CreditScore, Age, Tenure, Balance,
                          NumOfProducts, HasCrCard,
                          IsActiveMember, EstimatedSalary]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer Will Leave")
    else:
        st.success("Customer Will Stay")
      
