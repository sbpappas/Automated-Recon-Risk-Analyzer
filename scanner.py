import subprocess
import os

def run_scan(target, output_file="scan.xml"):
    
    is_root = os.geteuid() == 0 #check if running as root

    if is_root:
        scan_type = "-sS"  # stealthy little syn scan, this requires root priv
        os_flag = "-O"
        print("[+] Running privileged SYN scan")
    else:
        scan_type = "-sT"  # TCP connect scan, no root required
        os_flag = ""
        print("[!] Not running as root. Falling back to TCP connect scan")

    command = [
        "nmap", # main command
        scan_type, #syn (root) or tcp connect scan
        "-sV", # version detection
        "--script",
        "vuln",
        os_flag, # OS detection if root
        "-oX", # ouput in xml format, can also use -oN for normal or -oG for grepable
        output_file, # to this file
        target #the target IP
    ]

    print(f"[+] Running scan against {target}")
    print("[DEBUG] Command:", " ".join(command))
    result = subprocess.run(command)

    if result.returncode != 0:
        print("[!] Scan failed. Exiting.")
        exit(1)

    print("[+] Scan complete.")