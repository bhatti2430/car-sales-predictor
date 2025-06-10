import streamlit as st
import pickle
import pandas as pd

class CarSalesModel:
    def __init__(self, model_path: str, scaler_path: str):
        self.model = self.load_pickle(model_path)
        self.scaler = self.load_pickle(scaler_path)

    def load_pickle(self, path):
        with open(path, 'rb') as f:
            return pickle.load(f)

    def predict(self, input_data: pd.DataFrame) -> float:
        try:
            input_data = input_data.reindex(columns=self.model.feature_names_in_)
        except AttributeError:
            pass
        input_scaled = self.scaler.transform(input_data)
        return self.model.predict(input_scaled)[0]

class CarSalesApp:
    def __init__(self, model_path: str, scaler_path: str):
        self.model_obj = CarSalesModel(model_path, scaler_path)

    def run(self):
        st.title("🚗 Car Sales Prediction")
        st.write("Enter the details of the car to predict sales.")

        price = st.number_input("Price (in thousands)", min_value=0.0, value=25.0)
        engine_size = st.number_input("Engine Size (L)", min_value=0.0, value=2.0)
        horsepower = st.number_input("Horsepower", min_value=0.0, value=150.0)
        fuel_efficiency = st.number_input("Fuel Efficiency (MPG)", min_value=0.0, value=25.0)

        input_data = pd.DataFrame({
            "Price_in_thousands": [price],
            "Engine_size": [engine_size],
            "Horsepower": [horsepower],
            "Fuel_efficiency": [fuel_efficiency]
        })

        if st.button("Predict Sales"):
            prediction = self.model_obj.predict(input_data)
            st.success(f"Predicted Sales: **{prediction:.2f} units**")

# App automatically runs when script is executed
CarSalesApp('car_sales_model_svm.pkl', 'scaler.pkl').run()
