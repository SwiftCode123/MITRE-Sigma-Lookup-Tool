# TryHackMe - Security Operations Basics Writeup

## Overview

This writeup summarizes key concepts related to **Security Operations**, including the **SOC**, **Threat Intelligence**, **DFIR**, **Malware Analysis**, and **SIEM**.
The goal was to understand how security teams detect, analyze, and respond to cyber threats.

---

## Step 1: Security Operations Center (SOC)

A **SOC** monitors networks and systems to detect malicious activity and protect organizational infrastructure.

Key responsibilities:

* Monitor networks and systems for attacks
* Install **security patches and updates**
* Manage **vulnerabilities**
* Detect **policy violations** (ex: uploading company data to unauthorized cloud storage)
* Detect **unauthorized activity** such as stolen credentials
* Identify **network intrusions**

---

## Step 2: Threat Intelligence

**Threat Intelligence** focuses on gathering information about attackers to improve defense.

Threat intelligence process:

1. **Collection** – Gather data from internal and external sources
2. **Processing** – Convert data into a usable format
3. **Analysis** – Identify attacker behavior and motives
4. **Recommendations** – Provide defensive actions

Goal: **identify threat actors and predict future attacks**.

---

## Step 3: Digital Forensics & Incident Response (DFIR)

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

---

## Step 4: Malware Analysis

Malware analysis studies malicious software to understand its behavior.

Common malware types:

* **Virus** – attaches to programs and spreads by modifying files
* **Trojan** – appears legitimate but contains hidden malicious code
* **Ransomware** – encrypts files and demands payment

Analysis methods:

* **Static Analysis** – inspect malware without running it
* **Dynamic Analysis** – run malware in a controlled environment

---

## Step 5: SIEM

A **SIEM (Security Information and Event Management)** system collects and analyzes logs from multiple sources.

Functions:

* Centralized log collection
* Security monitoring dashboards
* Alert generation for suspicious activity

Challenge: analysts must investigate **true positives vs false positives**.

---

## Key Learning Points

* SOC teams continuously monitor systems for threats.
* Threat intelligence helps anticipate attacker behavior.
* DFIR investigates incidents and supports recovery.
* Malware analysis reveals how malicious software works.
* SIEM tools help detect suspicious activity through log analysis.
