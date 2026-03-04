from datetime import datetime

def generate_report(findings, output="report.md"):
    with open(output, "w") as f:
        f.write("# Security Assessment Report\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        f.write("## Findings\n\n")

        for item in findings:
            f.write(f"### Port {item['port']} - {item['service']}\n")
            f.write(f"- Product: {item['product']} {item['version']}\n")
            f.write(f"- Risk Level: {item['risk']}\n\n")

    print(f"[+] Report saved to {output}")
