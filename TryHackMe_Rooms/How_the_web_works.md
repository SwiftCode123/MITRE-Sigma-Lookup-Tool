## TryHackMe – DNS & How Websites Work Writeup

### Overview

This room explains how domain names are translated into IP addresses and how a website request travels through different components (DNS, web servers, load balancers, and databases) before content is displayed in the browser.

---

### Step 1: Domain Name System (DNS)

DNS translates human-readable domain names into IP addresses so computers can locate servers on the internet.

Domain structure includes:

* **Top Level Domain (TLD)** – The right-most part of a domain (e.g., `.com`, `.org`)
* **Second Level Domain (SLD)** – The main domain name (e.g., `tryhackme`)
* **Subdomain** – Additional prefixes like `admin.tryhackme.com`

Common DNS record types:

* **A** – Maps a domain to an IPv4 address
* **AAAA** – Maps a domain to an IPv6 address
* **CNAME** – Points one domain to another domain
* **MX** – Specifies the mail server responsible for emails
* **TXT** – Stores verification or security-related text data

---

### Step 2: DNS Resolution Process

When you enter a domain in a browser, several DNS servers help resolve the IP address.

The process typically follows:

1. Browser checks the **local DNS cache**
2. Query is sent to a **Recursive DNS Server**
3. If unknown, it queries the **Root DNS Server**
4. Root server directs it to the correct **TLD Server**
5. TLD server points to the **Authoritative DNS Server**
6. Authoritative server returns the correct **IP address**

The result is cached using a **TTL (Time To Live)** value for faster future lookups.

---

### Step 3: Web Infrastructure

Once the IP address is known, the request moves through several systems before reaching the website.

Key components include:

* **Web Application Firewall (WAF)** – Filters malicious or suspicious traffic
* **Load Balancer** – Distributes incoming traffic across multiple servers
* **Web Server** – Handles HTTP requests and serves website content
* **Database** – Stores dynamic data such as user accounts or blog posts
* **CDN (Content Delivery Network)** – Delivers cached content from servers closer to the user

---

### Step 4: Static vs Dynamic Content

Websites can serve two types of content:

**Static Content**

* Files that do not change (images, CSS, JavaScript)
* Delivered directly by the web server

**Dynamic Content**

* Generated based on user requests
* Often requires database queries

---

### Key Learning Points

* DNS converts domain names into IP addresses so browsers can locate servers.
* DNS resolution involves recursive, root, TLD, and authoritative servers.
* Modern websites rely on infrastructure such as **WAFs, load balancers, web servers, and databases** to handle traffic and deliver content efficiently.
* Understanding this flow is important in cybersecurity because attackers often target weak points in the web request process.
