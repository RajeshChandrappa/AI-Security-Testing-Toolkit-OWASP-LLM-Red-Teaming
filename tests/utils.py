import json
from datetime import datetime

def save_report(findings, filename="report.json"):
    """Save findings to a JSON file."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "findings": findings
    }
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"[+] Report saved to {filename}")
