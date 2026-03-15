# TryHackMe - Packets & Frames Writeup

## Overview
This room explains how data is transmitted across networks in small pieces called **packets** and **frames**.

---

## Step 1: Packets
- Data is divided into **packets** for transmission.  
- Each packet contains:
  - Source & destination IP
  - TTL (time to live)
  - Checksum (integrity verification)

---

## Step 2: Frames
- Operate at the **Data Link Layer**  
- Contain **MAC addressing information**  
- The process of adding headers is called **encapsulation**

---

## Step 3: TCP Three-Way Handshake
Before sending data via TCP:

1. **SYN:** Client requests connection  
2. **SYN-ACK:** Server acknowledges request  
3. **ACK:** Client confirms connection

Once complete, data transmission begins.

---

## Key Learning Points
- Packets and frames carry data along with addressing info.  
- Encapsulation ensures data integrity and proper delivery.  
- TCP connections use a three-way handshake for reliable communication.
