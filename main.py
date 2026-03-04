from scanner import run_scan
from parser import parse_scan
from risk_engine import assess_risk
from report_generator import generate_report

def main():
    target = input("Enter target IP: ")

    run_scan(target)
    services = parse_scan("scan.xml")
    findings = assess_risk(services)
    generate_report(findings)

if __name__ == "__main__":
    main()
