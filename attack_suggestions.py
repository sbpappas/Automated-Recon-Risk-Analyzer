def suggest_attacks(service, port, target):

    suggestions = []

    if service == "ftp":
        suggestions.append(f"Try anonymous login: ftp {target}")
        suggestions.append(f"Check anonymous access: nmap --script ftp-anon -p {port} {target}")

    elif service == "ssh":
        suggestions.append(f"Check for weak credentials: hydra -l root -P passwords.txt ssh://{target}")
        suggestions.append(f"Enumerate SSH algorithms: nmap --script ssh2-enum-algos -p {port} {target}")

    elif service == "http" or service == "https":
        suggestions.append(f"Run web scanner: nikto -h http://{target}:{port}")
        suggestions.append(f"Directory brute force: gobuster dir -u http://{target}:{port} -w wordlist.txt")

    elif service == "smb":
        suggestions.append(f"Enumerate shares: enum4linux {target}")
        suggestions.append(f"Check SMB vulnerabilities: nmap --script smb-vuln* -p {port} {target}")

    elif service == "mysql":
        suggestions.append(f"Attempt login: mysql -h {target} -u root -p")
        suggestions.append(f"Check MySQL info: nmap --script mysql-info -p {port} {target}")

    elif service == "rdp":
        suggestions.append(f"Check RDP security: nmap --script rdp-enum-encryption -p {port} {target}")

    return suggestions