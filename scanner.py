import subprocess
import os

def run_scan(target, output_file="scan.xml"):
    #check if running as root
    is_root = os.geteuid() == 0

    if is_root:
        scan_type = "-sS"  # stealthy little syn scan, this requires root priv
        print("[+] Running privileged SYN scan")
    else:
        scan_type = "-sT"  # TCP connect scan, no root required
        print("[!] Not running as root. Falling back to TCP connect scan")

    command = [
        "nmap", # main command
        scan_type, #syn (root) or tcp connect scan
        "-sV", # version detection
        "-O", # OS detection
        "-oX", # ouput in xml format
        output_file, # to this file
        target #the target IP
    ]

    print(f"[+] Running scan against {target}")
    result = subprocess.run(command)

    if result.returncode != 0:
        print("[!] Scan failed. Exiting.")
        exit(1)

    print("[+] Scan complete.")