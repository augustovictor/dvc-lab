import json
from typing import Dict, Any

SUMMARY_FILE_NAME = "summary.json"


def save_metrics(metrics: Dict[str, Any]):
    with open(SUMMARY_FILE_NAME, 'w') as f:
        json.dump(metrics, f)
