def assess_risk(service_info):
    risky_ports = {
        "21": "FTP - Often misconfigured",
        "23": "Telnet - Unencrypted",
        "445": "SMB - Lateral movement risk",
        "3306": "MySQL - Database exposure",
        "22": "SSH - Brute force target"
    }

    findings = []

    for service in service_info:
        port = service["port"]
        risk = "Low"

        if port in risky_ports:
            risk = "High"

        findings.append({
            **service,
            "risk": risk
        })

    return findings
