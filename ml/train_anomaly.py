import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("data/metrics.csv")

X = df[["cpu", "memory", "disk"]]

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

joblib.dump(model, "ml/anomaly_model.pkl")

print("Anomaly detection model trained & saved")
