# TryHackMe - Intro to LAN Writeup

## Overview
This room introduces **Local Area Networks (LANs)** and the devices that allow devices to communicate within a network.

---

## Step 1: IP Addresses
An **IP Address (Internet Protocol Address)** identifies devices on a network.

**Key points:**
- IPv4 addresses contain 4 octets (e.g., `192.168.1.1`)
- **Public IP:** assigned by ISP, communicates with the Internet
- **Private IP:** internal use, cannot directly access the Internet

---

## Step 2: MAC Addresses
A **MAC Address** is a unique hardware identifier on a device's Network Interface Card (NIC).

**Key points:**
- Used for local device identification
- Can be **spoofed** for impersonation attacks

---

## Step 3: LAN Topologies
**Network topology** describes how devices are physically connected.

**Star Topology**
- Devices connect to a central switch
- **Pros:** scalable, easy to add new devices  
- **Cons:** central switch failure can take down the network, more expensive

Here, we can see if the switch is broken (Single Point of Failure), everything stops working

![Alt text for the image](/Screenshots/star_top).png)

**Bus Topology**
- Devices share a single communication line
- **Pros:** simple and cost-efficient  
- **Cons:** single point of failure, can become slow with heavy traffic

Here, we can see if that the network is overwhelemed, the traffic can add up and slow the network down

![Alt text for the image](/Screenshots/bus_top.png)

**Ring Topology**
- Devices form a circular path for data
- **Pros:** requires less cabling, predictable data path  
- **Cons:** slower if multiple devices must be visited, prone to bottlenecks

Here, we can see that there can be bottlenecks and also if one area is cut/broken, the network is unable to send information around. Furthermore, it has to visit every device before reaching the intended device.

![Alt text for the image](/Screenshots/ring_top.png)

---

## Step 4: Networking Devices
**Switch**
- Connects devices within the same LAN using Ethernet
- **Pros:** efficient traffic management within LAN  
- **Cons:** cannot connect different networks by itself

**Router**
- Connects different networks and routes traffic between them
- **Pros:** enables Internet connectivity and subnet routing  
- **Cons:** configuration can be complex, single failure can disrupt traffic

---

## Key Learning Points
- IP addresses identify devices on a network.  
- MAC addresses uniquely identify hardware.  
- LAN topologies and devices determine how communication flows efficiently.  
- Understanding pros and cons of topologies helps design resilient networks.
