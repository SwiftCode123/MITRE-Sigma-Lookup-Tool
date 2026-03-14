# TryHackMe - Offensive Security Intro Writeup

## Overview
This is my writeup for the Offensive Security Intro room on TryHackMe. 
The goal of this task was to use directory enumeration to find hidden 
directories and exploit the bank transfer page.

---

## Step 1: Directory Enumeration

We start by using Gobuster to find hidden directories.

Command used:

gobuster dir -u http://fakebank.thm -w wordlist.txt

Explanation:
- gobuster → directory brute forcing tool
- -u → target URL
- -w → wordlist used for guessing directories
- dir → directory enumeration mode

Gobuster discovered the following directories:

/images  
/bank-transfer

[![Alt text for the image](/Screenshots/Offensive_Security/step_1)

---

## Step 2: Visiting the Discovered Directory

Navigate to:

http://fakebank.thm/bank-transfer

This page contains a bank transfer form that allows users to send money.

(Screenshot here)

---

## Step 3: Sending Money

Fill out the form:

Send From: Your account number  
Send To: Bank account number  
Amount: Any value  

Click **Send Money**.

(Screenshot here)

---

## Step 4: Confirming the Transfer

Return to the main page:

http://fakebank.thm

Refresh the page a few times and you will see your account balance updated.

This confirms the transfer was successful.

---

## Tools Used

- Gobuster
- Firefox

---

## Key Learning Points

- Directory enumeration is important for discovering hidden functionality.
- Gobuster can quickly brute force directories using a wordlist.
- Always check discovered endpoints for vulnerable functionality.
