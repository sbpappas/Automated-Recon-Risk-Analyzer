from scanner import run_scan
from parser import parse_scan
from risk_engine import assess_risk
from report_generator import generate_report
import os

def main():
    target = input("Enter target IP: ")

    run_scan(target) # create file
    if not os.path.exists("scan.xml"): #be safe and check
        print("[!] No scan results found. Exiting.")
        return
    
    services = parse_scan("scan.xml") # parse file
    findings = assess_risk(services) #analyze data
    generate_report(findings) #create pretty report

if __name__ == "__main__":
    main()
