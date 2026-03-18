from scanner import run_scan
from parser import parse_scan
from risk_engine import assess_risk
from report_generator import generate_report
from attack_suggestions import suggest_attacks
from cve_lookup import lookup_cves  
import os

# Run with python3 main.py or sudo python3 main.py if you want to run nmap with root privileges
# then type in your target IP address and wait for report generation (127.0.0.1 is a good test)

def main():
    target = input("Enter target IP: ")

    run_scan(target) # create file
    if not os.path.exists("scan.xml"): #be safe and check
        print("[!] No scan results found. Exiting.")
        return
    
    print("Parsing scan results...")
    services = parse_scan("scan.xml") # parse file
    findings = assess_risk(services) #analyze data
    print("Creating attack suggestions...")
    for item in findings:
        item["suggestions"] = suggest_attacks(
            item["service"],
            item["port"],
            target
        )
        item["cves"] = lookup_cves(
            item["product"],
            item["version"]
        )
    print("Generating report...")
    generate_report(findings) #create pretty report
    print_results(findings, target) #nice output in CLI

def print_results(findings, target):
    print(f"\n[+] Scan Results for {target}\n")

    for item in findings:
        port = item["port"]
        service = item["service"]
        risk = item["risk"]

        print(f"[OPEN] Port {port} ({service}) - {risk} Risk")

        if item.get("cves"):
            for cve in item["cves"]:
                print(f"    [CVE] {cve}") # still might need some improvement

        if item.get("suggestions"):
            for suggestion in item["suggestions"]:
                print(f"    → {suggestion}")

        print()

if __name__ == "__main__":
    main()
