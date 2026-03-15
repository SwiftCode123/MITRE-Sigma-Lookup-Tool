# TryHackMe - Security Operations Basics Writeup

## Overview

This writeup summarizes key concepts related to **Security Operations**, including the **SOC**, **Threat Intelligence**, **DFIR**, **Malware Analysis**, and **SIEM**.
The goal was to understand how security teams detect, analyze, and respond to cyber threats.

---

## Security Operations Center (SOC)

A **SOC** monitors networks and systems to detect malicious activity and protect organizational infrastructure.

Key responsibilities:

* Monitor networks and systems for attacks
* Install **security patches and updates**
* Manage **vulnerabilities**
* Detect **policy violations** (ex: uploading company data to unauthorized cloud storage)
* Detect **unauthorized activity** such as stolen credentials
* Identify **network intrusions**

---

## Threat Intelligence

**Threat Intelligence** focuses on gathering information about attackers to improve defense.

Threat intelligence process:

1. **Collection** – Gather data from internal and external sources
2. **Processing** – Convert data into a usable format
3. **Analysis** – Identify attacker behavior and motives
4. **Recommendations** – Provide defensive actions

Goal: **identify threat actors and predict future attacks**.

---

## Digital Forensics & Incident Response (DFIR)

**DFIR** focuses on investigating digital crimes and responding to security incidents.

Evidence sources:

* File systems (installed programs, modified files)
* **System memory** (malware running only in RAM)
* System and network logs

Incident Response phases:

1. **Preparation**
2. **Detection & Analysis**
3. **Containment, Eradication, Recovery (CER)**
4. **Post-Incident Activity**

![Alt text for the image](/Screenshots/PDA_CER.png)
---

## Malware Analysis

Malware analysis studies malicious software to understand its behavior.

Common malware types:

* **Virus** – attaches to programs and spreads by modifying files
* **Trojan** – appears legitimate but contains hidden malicious code
* **Ransomware** – encrypts files and demands payment

Analysis methods:

* **Static Analysis** – inspect malware without running it
* **Dynamic Analysis** – run malware in a controlled environment

---

## SIEM

A **SIEM (Security Information and Event Management)** system collects and analyzes logs from multiple sources.

Functions:

* Centralized log collection
* Security monitoring dashboards
* Alert generation for suspicious activity

Challenge: analysts must investigate **true positives vs false positives**.

## LAB

Step 1: I identified that there were multiple logs here. However, one stuck out where it said "Unauthorized connection" by the IP address 143.110.250.149. The other logs seemed like normal activity or false positives.
![Alt text for the image](/Screenshots/SOC_step1.png)

Step 2: This involved scanning the IP address and making sure it was actual malicious and I found out it was malicious by typing in the IP address 143.110.250.149
![Alt text for the image](/Screenshots/SOC_step2.png)

Step 3: I needed to escalate this situation to the proper staff member which was the SOC team lead 
![Alt text for the image](/Screenshots/SOC_step3.png)

Step 4: We got permission to block this specific IP address and achieved the flag
![Alt text for the image](/Screenshots/SOC_step4.png)

---

## Key Learning Points

* SOC teams continuously monitor systems for threats.
* Threat intelligence helps anticipate attacker behavior.
* DFIR investigates incidents and supports recovery.
* Malware analysis reveals how malicious software works.
* SIEM tools help detect suspicious activity through log analysis.
* Basic idea of how SOC analysts work with detecting, analyzing, escalating, blocking and then documentation
