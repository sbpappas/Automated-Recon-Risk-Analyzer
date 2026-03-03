import subprocess

def run_scan(target, output_file="scan.xml"):
    command = [
        "nmap",
        "-sS",
        "-sV",
        "-O",
        "-oX",
        output_file,
        target
    ]

    print(f"[+] Running scan against {target}")
    subprocess.run(command)
    print("[+] Scan complete.")
