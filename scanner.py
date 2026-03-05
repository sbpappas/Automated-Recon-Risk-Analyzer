import subprocess
import os

def run_scan(target, output_file="scan.xml"):
    # heck if running as root
    is_root = os.geteuid() == 0

    if is_root:
        scan_type = "-sS"  # SYN scan (stealthy)
        print("[+] Running privileged SYN scan")
    else:
        scan_type = "-sT"  # TCP connect scan (no root required)
        print("[!] Not running as root. Falling back to TCP connect scan")

    command = [
        "nmap",
        scan_type,
        "-sV",
        "-O",
        "-oX",
        output_file,
        target
    ]

    print(f"[+] Running scan against {target}")
    result = subprocess.run(command)

    if result.returncode != 0:
        print("[!] Scan failed. Exiting.")
        exit(1)

    print("[+] Scan complete.")