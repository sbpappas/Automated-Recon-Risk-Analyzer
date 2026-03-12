import subprocess
import os

def run_scan(target, output_file="scan.xml"):
    
    is_root = os.geteuid() == 0 #check if running as root

    command = [
        "nmap",
        "-sV",
        #"--script", "vuln", # nse was taking too long
        "-oX", output_file
    ]

    if is_root:
        print("[+] Running privileged SYN scan")
        command.insert(1, "-sS")
        command.append("-O")
    else:
        print("[!] Not running as root. Falling back to TCP connect scan")
        command.insert(1, "-sT")

    command.append(target)

    print(f"[+] Running scan against {target}")
    print("[DEBUG] Command:", " ".join(command))
    result = subprocess.run(command)

    if result.returncode != 0:
        print("[!] Scan failed. Exiting.")
        exit(1)

    print("[+] Scan complete.")