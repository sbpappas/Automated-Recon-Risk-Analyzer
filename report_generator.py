from datetime import datetime

def generate_report(findings, output="report.md"):

    with open(output, "w") as f:

        f.write("# Security Assessment Report\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        for item in findings:

            f.write(f"## Port {item['port']} ({item['service']})\n")
            f.write(f"Product: {item['product']} {item['version']}\n")
            f.write(f"Risk Level: {item['risk']}\n\n")

            if item["vulnerabilities"]:
                f.write("### Detected Vulnerabilities\n")

                for vuln in item["vulnerabilities"]:
                    f.write(f"- {vuln['id']}: {vuln['output']}\n")

                f.write("\n")
            
            if "suggestions" in item and item["suggestions"]:
                f.write("### Suggested Next Steps\n")

                for suggestion in item["suggestions"]:
                    f.write(f"- {suggestion}\n")

                f.write("\n")

    print(f"[+] Report saved to {output}")