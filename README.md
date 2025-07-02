🔍 Nmap Payload Generator – CLI-Based Network Scanner
A Linux-based interactive Python tool to generate and execute customized Nmap payloads for network scanning, OS detection, and vulnerability assessment.

🚀 Features
Interactive CLI menu to build Nmap commands

Supports:

TCP SYN, UDP, and ACK scans

Host discovery techniques

OS and version detection

NSE script selections (safe, vuln, intrusive)

Custom scan speeds (T0 to T5)

Saves scan output to nmap_report.txt

Designed for use in ethical hacking labs or CTF practice

Written in pure Python with subprocess module

🛠️ Technologies Used
🐍 Python 3

📡 Nmap (must be installed on the system)

💻 Linux Terminal (tested on Kali Linux)

📦 Requirements
Python 3.x

Nmap installed (sudo apt install nmap on Debian/Kali)

Linux OS (preferred)

📁 Installation
bash
Copy
Edit
git clone https://github.com/your-username/nmap-payload-generator.git
cd nmap-payload-generator
chmod +x script_name.py
python3 script_name.py
Replace script_name.py with the actual filename, e.g. nmap_generator.py.

📸 Sample Screenshot
(Add a screenshot here showing your terminal running the tool)

📝 Usage
Run the script using Python 3.

Follow the on-screen menus to:

Select scan type

Choose host discovery method

Enable/disable OS detection, NSE scripts, etc.

Enter the target IP address or range.

The script will run the final Nmap command and save the output to nmap_report.txt.

⚠️ Disclaimer
This tool is intended for educational and ethical use only. Do not scan any networks or devices without proper authorization.

