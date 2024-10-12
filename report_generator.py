import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, log_file="anomaly_log.json"):
        self.log_file = log_file

    def log_anomaly(self, data, anomaly_type):
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'anomaly_type': anomaly_type,
            'data': data
        }
        with open(self.log_file, "a") as f:
            json.dump(log_entry, f)
            f.write("\\n")
