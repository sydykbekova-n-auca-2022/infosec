Course: Information Security (Spring 2026)
Professor: Gulzada Esenalieva
Student: Nurkyz Sydykbekova

⚖️ Ethical Disclosure & Consent
I confirm that I am aware of my actions and responsible for the commands executed in this course. > All projects contained in this repository were developed in a controlled, local environment for educational purposes. These tools are designed to demonstrate vulnerabilities and defensive strategies, not for unauthorized use.

📂 Repository Structure
This repository contains a series of laboratory assignments focusing on Python development, API security, and penetration testing concepts.

Lab #	Focus Area	Description
Lab 1-11	Python Foundations	Basics of logic, loops, data structures, and file handling.
Lab 12	C2 Server (Backend)	A FastAPI server acting as a Command & Control (C2) listener.
Lab 13	Malware Simulation	A keyboard listener (Keylogger) with automated data exfiltration.
🏗️ Featured Project: The Attack Chain (Lab 12 & 13)
The most advanced portion of this repository demonstrates how a threat actor can capture user data and send it to a remote server.

📡 System Architecture
The Victim (Lab 13): A Python script runs a background listener using the pynput library. Every keystroke is logged locally to log.txt.
The Trigger: Upon a specific event (pressing the Esc key), the script initiates an HTTP POST request.
The Exfiltration: Using the requests library, the logged data is sent over the network to a specific API endpoint.
The Attacker (Lab 12): A FastAPI server receives the incoming data via the /report endpoint and saves it to stolen_data.txt for later review.
🛠️ Installation & Setup
Prerequisites
Python 3.9+
macOS / Linux / Windows
Virtual Environment (venv)
1. Clone the Repository
Bash
git clone https://github.com/sydykbekova-n-auca-2022/infosec.git
cd infosec
2. Configure Environments
Each lab folder contains its own venv. To run the Integrated Attack:

Bash
# Terminal 1: Start the Listener
cd lab12
source venv/bin/activate
python3 -m uvicorn main:app --port 8000

# Terminal 2: Run the Keylogger
cd lab13
source venv/bin/activate
python3 main.py
🔍 Key Learning Outcomes
API Development: Building RESTful endpoints with FastAPI to handle Form data.
Input Hooking: Understanding how operating systems handle keyboard events and security permissions.
Network Communication: Implementing the requests library to simulate data exfiltration.
Troubleshooting: Navigating macOS Privacy & Security (Accessibility) settings and managing Python Path/Shell function conflicts.
