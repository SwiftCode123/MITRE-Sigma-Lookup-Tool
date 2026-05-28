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

Below we can see the successful run for Technique ID `T15661`. This printed out a comprehensive description of what phishing is (adversaries sending malicious messages to gain access to victim systems, utilizing social engineering, spearphishing, malicious attachments, or links). It also displayed a mitigation table of how to defend against phising such as `Audit (M1047)`, `Network Intrusion Prevention (M1031)`, `Software Configuration (M1054)`, `Restrict Web-Based Content (M1021)`, `Antivirus/Antimalware (M1049)`, and `User Training (M1017)`. 

The Sigma rules tables describes the attempt to find code that can detect phishing attempts. For example, the script found files in the local folders, `proc_creation_win_office_outlook_execution_from_temp.yml and iso_phishing.yml` that contain the text `T15661`. There are also many `no titles` and this is because the script had trouble reading some of the internal YAML fields and so it could not extract the rule titles and instead showed the default placeholders. However, we see one rule parsed correct named `Search-ms and WebDAV Suspicious Indicators in URL`

This is a name of a Sigma detection rule that is designed to detect phising links that abuse Windows feature such as `search-ms` and `WebDAV`. Attackers sometimes use these technologies to trick users into opening malicious files or connecting to attacker-controlled servers. 

`search-ms` is a Windows protocol that opens the Windows Search feature.
Attackers can craft malicious links that look harmless but actually open remote content. `WedDAV` is a protocol that lets remote web servers behave like shared network drives.
Attackers can host malware on a WebDAV server so the victim’s computer treats it like a normal file share. For example, a phising email might contain `search-ms:query=invoice` or connect to a remote WebDAV location. The Sigma rule watches logs for these suspicious URL patterns because they are commonly used in phishing and malware delivery campaigns

<img width="6412" height="10076" alt="mitre_ID" src="https://github.com/user-attachments/assets/e95e816f-8da4-4d50-b89d-1f8c3edd9075" />

### Searching by Technique name

Instead of searching by Technique ID, we can also search by technique name. I chose `Masquerading (T1036)` where hackers disguise malicious files or activity as something completely harmless (like renaming a piece of malware to svchost.exe so it looks like a built-in Windows service). The mitigations and sigma rules are outputted as well and describe the ways to defend and detect these attacks

For example, we can see that one mitigation technique is `Code Signing (M1045)` where we ensure files have a valid digital signature so hackers can't easily fake standard system utilities

The sigma output shows us ways to detect this attack. In these rules `proc_creation_win_renamed_powershell.yml` and `proc_creation_win_renamed_psexec.yml` monitor Windows event logs to see if a process has been renamed to hide its identity

<img width="5367" height="16384" alt="mitre_name" src="https://github.com/user-attachments/assets/e3ebc8cc-aefc-4253-b852-c2c4aa461d4d" />

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

 ## Post Project Implmentation #1: Alias
- I decided to add this improvement as the first one. Creating an alias is very helpful instead of typing out long commands in the terminal
	- To make it a standalone command, we need to give the file execute permissions. This is because Unix systems require execute permissions before a script 	  can be run directly from the terminal. This change was made via `chmod +x mitre-attack-sigma.py`
 	- Next, I opened my configuration file via `nano ~/.zshrc` and added my alias starting          with the command `alias mitre=[MY PATH]`. Since I am in a 	virtual environment and my 		script relies on packages such as `rich` and `yaml` inside my `venv`, a standard alias 		might fail if the virtual environment isn't active. I fixed this by pointing the alias 		directly to the Python interpreter inside my venv. I saved it via `source ~/.zshrc` and 	tested it with `mitre Masquerading`. Below are the results and it worked. As you can see instead of having to `cd` inside folders and provide a long command, I can just type `mitre` which is the alias and it works the same way as it did before. Note that I also do not need to be inside the `venv` folder and can deactivate it and it still works
<img width="5192" height="6508" alt="image" src="https://github.com/user-attachments/assets/afff9932-114d-4515-b1d2-c543568f4c9d" />
