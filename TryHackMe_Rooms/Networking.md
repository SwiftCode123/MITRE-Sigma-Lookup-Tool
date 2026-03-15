# TryHackMe - What is Networking? Writeup

## Overview
This room introduces the fundamentals of networking, explaining how devices connect and communicate across networks and the Internet.

---

## Step 1: Understanding Networks
A **network** is a collection of devices connected together to share data and resources.

**Examples:**
- Home Wi-Fi networks
- School or company networks
- Data center infrastructure

Networks allow devices to communicate efficiently and share resources.

---

## Step 2: The Internet
The **Internet** is the largest network in the world, made up of many smaller networks connected together.

**Important points:**
- Early Internet development started with **ARPANET**
- The **World Wide Web (WWW)** was created by **Tim Berners-Lee**
- Connects private networks through a global **public network infrastructure**

---

## Step 3: Private vs Public Networks
**Private Network**
- Internal networks such as home Wi-Fi
- Devices communicate only within the network

**Public Network**
- Networks accessible to the public, e.g., café Wi-Fi
- Higher security risk compared to private networks

## LAB
- Here, we can spoof the MAC address of the other device and pretend to be them
Step 1: See what works
![Alt text for the image](/Screenshots/Network_step1.png)
![Alt text for the image](/Screenshots/Network_step2.png)

Step 2: We can change the MAC address to the other device and send the data to get the flag

![Alt text for the image](/Screenshots/Network_step3.png)

Basic Ping command such as where we can ping Google's public DNS resolver via the command 
`ping -c 4 8.8.8.8 ` which means send 4 count of packets to the 8.8.8.8
![Alt text for the image](/Screenshots/ping.png)

---

## Key Learning Points
- Networks connect multiple devices to share information.
- The Internet is a global network composed of smaller networks.
- Understanding networking basics is critical for cybersecurity roles.
