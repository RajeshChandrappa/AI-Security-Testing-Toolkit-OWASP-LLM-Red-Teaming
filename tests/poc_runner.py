#!/usr/bin/env python3
"""
AI Security Testing Toolkit – Main Runner
Usage:
    python poc_runner.py --category LLM02 --mode prompt
    python poc_runner.py --generate-report
"""

import argparse
import json
import sys
from datetime import datetime

# Import test modules
from test_llm01_prompt_injection import run as run_llm01
from test_llm02_sensitive_info_disclosure import run as run_llm02
from test_llm03_supply_chain import run as run_llm03
from test_llm04_denial_of_service import run as run_llm04
from test_llm05_model_theft import run as run_llm05
from test_llm06_excessive_agency import run as run_llm06
from test_llm07_system_prompt_leakage import run as run_llm07
from test_llm08_vector_store_injection import run as run_llm08
from test_llm09_misinformation import run as run_llm09
from test_llm10_unbounded_consumption import run as run_llm10

TESTS = {
    "LLM01": run_llm01,
    "LLM02": run_llm02,
    "LLM03": run_llm03,
    "LLM04": run_llm04,
    "LLM05": run_llm05,
    "LLM06": run_llm06,
    "LLM07": run_llm07,
    "LLM08": run_llm08,
    "LLM09": run_llm09,
    "LLM10": run_llm10,
}

def generate_report(findings):
    report = {
        "timestamp": datetime.now().isoformat(),
        "findings": findings
    }
    with open("security_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("[+] Report saved to security_report.json")
    print("\n--- SUMMARY ---")
    for f in findings:
        print(f"[!] {f}")

def main():
    parser = argparse.ArgumentParser(description="AI Security Testing Toolkit")
    parser.add_argument("--category", help="OWASP LLM category (e.g., LLM02)")
    parser.add_argument("--mode", choices=["prompt", "auto"], default="prompt")
    parser.add_argument("--generate-report", action="store_true")
    args = parser.parse_args()

    if args.generate_report:
        demo_findings = [
            "Python version disclosed: 3.12.11",
            "OS/kernel disclosed: Linux 6.8.0-1044-gke",
            "Installed packages: 89 (cryptography==46.0.6, etc.)",
            "Environment variable names with 'KEY' disclosed: 24",
            "Code execution allowed: listed current directory",
            "Long output accepted: 200+ repetitions"
        ]
        generate_report(demo_findings)
        return

    if args.category and args.category in TESTS:
        TESTS[args.category]()
    else:
        print("Available categories: " + ", ".join(TESTS.keys()))
        sys.exit(1)

if __name__ == "__main__":
    main()
