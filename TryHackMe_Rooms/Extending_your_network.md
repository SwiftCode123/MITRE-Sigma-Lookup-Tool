# TryHackMe - Extending Your Network Writeup

## Overview
This room covers technologies for extending and securing networks, including **ports, firewalls, VPNs, and port forwarding**.

---

## Step 1: Ports
- Communication endpoints for services
- Common ports:
  - FTP → 21
  - SSH → 22
  - HTTP → 80
  - HTTPS → 443
  - SMB → 445
  - RDP → 3389
- Ports range: 0 – 65535

---

## Step 2: Port Forwarding
- Allows internal network services to be accessed externally  
- Example: hosting a web server internally and forwarding port 80 to the Internet  

---

## Step 3: Firewalls
- Monitor and filter incoming/outgoing traffic  
- **Stateful firewall:** analyzes entire connections  
- **Stateless firewall:** inspects individual packets

---

## Step 4: VPN
- Creates encrypted tunnels for secure communication over the Internet  
- Benefits: privacy, security, remote network access  
- Technologies: PPTP, IPSec

## LAB
Step 1: Properly Configure the firewall rule with Source IP address of `192.51.100.34` and destination IP address of `203.0.110.1` on port 80 and the action would be to DROP aka block the connection

![Alt text for the image](/Screenshots/firewall_step2.png)

Step 2: Add the rule and activate the rule and retrieve the flag

![Alt text for the image](/Screenshots/firewall_step3.png)

---

## Key Learning Points
- Ports allow services to communicate.  
- Firewalls protect networks by filtering traffic.  
- VPNs create secure connections over public networks.
