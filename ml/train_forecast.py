import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib


df = pd.read_csv("data/metrics.csv")


df["cpu_prev"] = df["cpu"].shift(1)
df.dropna(inplace=True)

X = df[["cpu_prev"]]
y = df["cpu"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "ml/cpu_forecast.pkl")

print("CPU forecast model trained & saved")
