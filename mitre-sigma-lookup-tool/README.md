#  MITRE-Sigma Lookup Tool

CLI tool to lookup the MITRE mitigations and the Sigma detections for any technique
## Project Background

**MITRE ATT&CK** is a globally accessible knowledge base of adversary tactics and techniques. Security teams use it to understand attacker behaviors, plan defenses, and map observed activity in their networks.

**Sigma** is a generic and open signature format for SIEM (Security Information and Event Management) systems. It allows security teams to define detection rules once and convert them to different SIEM formats. By linking ATT&CK techniques to Sigma rules, analysts can quickly translate threat intelligence into actionable detection logic.

Through this project, I will interact with ATT&CK data, extract useful information, and gain hands-on exposure to practical cybersecurity workflows while developing my Python and Linux skills.

## Project Specifications

Input: an ATT&CK technique ID (`T1564`) or technique name.

Output:
	- Basic technique info (name, description)
	- ATT&CK mitigations related to that technique
	- Sigma rules that mention the technique ID

### Dependencies
Python 3.9+

A Linux environment with Internet access

*Note this project can be done in other systems, however all instructions are intended for Linux and may need to be modified for other environments.*
	
## Setup Environment

The setup process has been automated with `setup.sh`, or you can follow these steps:

### 1. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```
### 2. Install libraries
```bash
pip install mitreattack-python pyyaml rich
```

https://mitreattack-python.readthedocs.io/en/latest/
### 3. Download an ATT&CK STIX bundle file (enterprise)
```bash
curl https://raw.githubusercontent.com/mitre-attack/attack-stix-data/refs/heads/master/enterprise-attack/enterprise-attack.json -o enterprise-attack.json
```
### 4. Clone SigmaHQ/sigma locally
```bash
git clone https://github.com/SigmaHQ/sigma.git
```
### 5. Create a hello world program in `lookup.py`
```bash
echo -e '#!/usr/bin/env python3\nprint("hello world")' > lookup.py
```

## Example Usage
### Searching by Technique ID

<img width="6412" height="10076" alt="mitre_ID" src="https://github.com/user-attachments/assets/e95e816f-8da4-4d50-b89d-1f8c3edd9075" />

## Post Project Ideas

- Alias the program to create a custom command that is accessible anywhere
- Handle outputting to files
- Handle bulk searches and outputs
- Integrate another open-source library mapped to MITRE ATT&CK
- Use Django to create a web interface
	- Search bar for searching, rather than command line argument
	- Host static site via cloud technology or physical server
- Improve the speed of Sigma searches 
	- maybe by applying particular data structures & algorithms
- Automatically update MITRE and Sigma (which are only accessed locally)
- Make searching by name or description “smarter” 
	- Output all techniques that partially map to description and let user choose
- Interface directly with other professional cybersecurity tools
	- MITRE Caldera - Attack platform for launching TTPs in MITRE ATT&CK
	- Metasploit - Tool for emulating attacker’s TTPs
	- Splunk - Open-source SIEM (could implement Sigma rules directly)
