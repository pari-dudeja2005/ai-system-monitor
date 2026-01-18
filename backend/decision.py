# backend/decision.py
import statistics


history = []
MAX_HISTORY = 20  

def analyze_metrics(cpu, memory, disk):
    """
    Returns predicted CPU, anomaly detection, and alert status.
    """
   
    history.append(cpu)
    if len(history) > MAX_HISTORY:
        history.pop(0)

    
    predicted_cpu = round(statistics.mean(history), 2)

   
    if len(history) > 1:
        mean = statistics.mean(history)
        std_dev = statistics.stdev(history)
        anomaly = cpu > mean + 2 * std_dev
    else:
        anomaly = False

    
    alert = cpu > 80 or anomaly

    return {
        "predicted_cpu": predicted_cpu,
        "anomaly": anomaly,
        "alert": alert
    }


