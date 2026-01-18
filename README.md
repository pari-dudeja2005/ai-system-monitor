# AI System Monitor

Real-time system monitoring dashboard with **AI-powered CPU prediction and anomaly alerts**.  
This project collects system metrics (CPU, memory, disk), predicts CPU trends, and triggers alerts when anomalies occur. Built with Python, FastAPI, and React.js.

---

## 🏗️ Architecture

[Collector] --> [Backend / FastAPI] --> [Frontend / React Dashboard]
| |
psutil data ML logic: CPU prediction & anomaly detection
|
Mock Alerts (Slack / PagerDuty)

- **Collector**: Collects system metrics every 2 seconds using Python `psutil` and sends them to the backend  
- **Backend**: FastAPI server handles metrics ingestion, runs prediction & anomaly detection, and triggers mock alerts  
- **Frontend**: React dashboard shows live CPU usage, predicted CPU, and alert status  

---

## ✨ Features

- Real-time CPU, memory, and disk monitoring  
- CPU prediction using moving average  
- Anomaly detection (spikes)  
- Alerts system (mock Slack & PagerDuty)  
- Interactive live chart with tooltips  
- Clean, professional frontend for demo  

---

## ⚡ Tech Stack

- **Backend**: Python, FastAPI  
- **Frontend**: React.js, Recharts, Axios  
- **AI**: Moving average CPU prediction + anomaly detection  
- **Alerts**: Mock Slack & PagerDuty alerts  

---

## 🚀 Setup & Run Instructions

1️⃣ Clone the repo

git clone https://github.com/pari-dudeja2005/ai-system-monitor.git
cd ai-system-monitor


2️⃣ Setup Python environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


3️⃣ Run Backend (FastAPI)

uvicorn backend.main:app --reload


4️⃣ Run Collector (metrics sender)

python collector/collector.py


5️⃣ Run Frontend (React Dashboard)

cd frontend
npm install
npm start
<img width="1325" height="696" alt="Screenshot 2026-01-18 at 8 45 10 PM" src="https://github.com/user-attachments/assets/80b42ca1-7270-4a8f-b7a4-18ce3c931805" />

