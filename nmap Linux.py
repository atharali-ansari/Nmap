#!/usr/bin/python3

import subprocess
from time import sleep

def main_menu():
    subprocess.run("clear")
    print("MENU")
    print()
    print("[1] - Create Payload")
    print("[2] - See Templates")
    print("[3] - Exit")
    response = input("> ")
    if response == '1':
        create()
    elif response == '2':
        templates()
    elif response == '3':
        print("Goodbye!")
    else:
        print("Invalid Input")
        main_menu()

def create():
    payload = "sudo nmap"
    subprocess.run("clear")
    print("Scan Type:")
    print('''
[1] - TCP SYN port scan (Default)
[2] - TCP connect port scan (Default without root privilege)
[3] - UDP port scan
[4] - TCP ACK port scan
[5] - TCP Window port scan
[6] - TCP Maimon port scan
[7] - Skip
    ''')
    response = input("> ")
    dictionary = {
        '1': '-sS',
        '2': '-sT',
        '3': '-sU',
        '4': '-sA',
        '5': '-sW',
        '6': '-sM',
        '7': '',
    }
    payload += ' ' + dictionary.get(response, '')

    subprocess.run("clear")
    print("Host Discovery:")
    print('''
[1] - No Scan. List targets only
[2] - Disable port scanning. Host discovery only.
[3] - Disable host discovery. Port scan only.
[4] - TCP SYN discovery on port x. Port 80 by default
[5] - TCP ACK discovery on port x. Port 80 by default
[6] - UDP discovery on port x. Port 40125 by default
[7] - ARP discovery on local network
[8] - Never Do DNS resolution
[9] - Skip
    ''')
    response = input("> ")
    dictionary = {
        '1': '-sL',
        '2': '-sn',
        '3': '-Pn',
        '4': '-PS',
        '5': '-PA',
        '6': '-PU',
        '7': '-PR',
        '8': '-n',
        '9': '',
    }
    payload += ' ' + dictionary.get(response, '')

    subprocess.run("clear")
    print("Service and Version Detection:")
    print('''
[1] - Detect OS
[2] - Detect Version of service
[3] - Enables OS detection, version detection, script scanning, and traceroute
[4] - Skip
    ''')
    response = input("> ")
    dictionary = {
        '1': '-O',
        '2': '-sV',
        '3': '-A',
        '4': '',
    }
    payload += ' ' + dictionary.get(response, '')

    subprocess.run("clear")
    print("Scan Speed:")
    print('''
[1] - Paranoid (Intrusion Detection System evasion)
[2] - Sneaky (Intrusion Detection System evasion)
[3] - Polite (uses less bandwidth and resources)
[4] - Normal (default speed)
[5] - Aggressive (faster scan)
[6] - Insane (fastest scan)
[7] - Skip
    ''')
    response = input("> ")
    dictionary = {
        '1': '-T0',
        '2': '-T1',
        '3': '-T2',
        '4': '-T3',
        '5': '-T4',
        '6': '-T5',
        '7': '',
    }
    payload += ' ' + dictionary.get(response, '')

    subprocess.run("clear")
    print("Scripts:")
    print('''
[1] - Scan with default NSE scripts (safe)
[2] - Scan for vulnerabilities
[3] - Use only safe scripts
[4] - Use intrusive scripts (unsafe)
[5] - Skip
    ''')
    response = input("> ")
    dictionary = {
        '1': '-sC',
        '2': '--script=vuln',
        '3': '--script=safe',
        '4': '--script=intrusive',
        '5': '',
    }
    payload += ' ' + dictionary.get(response, '')

    print()
    print(f"Your payload is: {payload}")

    # Prompt for IP address or range
    ip_address = input("Enter the target IP address or range: ")

    # Run the Nmap command with the payload and verbose mode
    final_command = f"{payload} -v {ip_address}"
    print(f"Running: {final_command}")

    # Save output to a file
    output_file = "nmap_report.txt"
    with open(output_file, "w") as file:
        subprocess.run(final_command.split(), stdout=file)

    print(f"Scan complete! Report saved to {output_file}.")

def templates():
    print("Copy one of the below payloads and replace '<IP address/range>'")
    print("nmap <IP address/range>")
    print("nmap -p- -A <IP address/range>")
    print("nmap -sS -Pn -A <IP address/range>")

main_menu()
