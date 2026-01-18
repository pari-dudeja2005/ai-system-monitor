import time
import psutil
import requests

BACKEND_URL = "http://localhost:8000/ingest"
INTERVAL = 2  

print("Starting system metrics collector...")

while True:
    data = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "timestamp": time.time()
    }

    print(data)  

    try:
        response = requests.post(BACKEND_URL, json=data)
        if response.status_code != 200:
            print("Error sending data:", response.status_code, response.text)
    except Exception as e:
        print("Backend not reachable:", e)

    time.sleep(INTERVAL)


