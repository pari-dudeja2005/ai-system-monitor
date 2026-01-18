from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.decision import analyze_metrics
from backend.alerts import slack, pagerduty

app = FastAPI(title="AI System Monitor Backend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Metrics(BaseModel):
    cpu: float
    memory: float
    disk: float
    timestamp: float


latest_data = {}

@app.post("/ingest")
def ingest(metrics: Metrics):
    """
    Collect metrics, analyze them, and trigger alerts if needed.
    """
    result = analyze_metrics(metrics.cpu, metrics.memory, metrics.disk)

   
    latest_data.update({
        "cpu": metrics.cpu,
        "memory": metrics.memory,
        "disk": metrics.disk,
        "timestamp": metrics.timestamp,
        **result
    })

    
    if result["alert"]:
        message = f"ALERT! CPU spike detected: {metrics.cpu}%"
        slack.send_slack_alert(message)
        pagerduty.send_pagerduty_alert(message)

    return {"status": "ok"}

@app.get("/metrics/latest")
def get_latest():
    """
    Return latest collected metrics for frontend.
    """
    return latest_data




