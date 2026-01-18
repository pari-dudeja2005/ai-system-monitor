import joblib
import numpy as np

forecast_model = joblib.load("ml/cpu_forecast.pkl")
anomaly_model = joblib.load("ml/anomaly_model.pkl")

def predict_next_cpu(last_cpu):
    return forecast_model.predict([[last_cpu]])[0]

def detect_anomaly(cpu, memory, disk):
    pred = anomaly_model.predict([[cpu, memory, disk]])
    return pred[0] == -1  
