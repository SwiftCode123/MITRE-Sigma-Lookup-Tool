## TryHackMe – DNS & How Websites Work Writeup

### Overview

This room explains how domain names are translated into IP addresses and how a website request travels through different components (DNS, web servers, load balancers, and databases) before content is displayed in the browser.

---

### Step 1: Domain Name System (DNS)

DNS translates human-readable domain names into IP addresses so computers can locate servers on the internet.

Domain structure includes:

* **Top Level Domain (TLD)** – The right-most part of a domain (`.com`, `.org`)
* **Second Level Domain (SLD)** – The main domain name (`tryhackme`)
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
## LAB

Step 1: Here, we needed to get a CNAME record and I selected CNAME and typed in the name `shop` which gave us shop.website.thm retrieving the flag. Note that the CNAME record points one domain to another domain by definition.

![Alt text for the image](/Screenshots/CNAME.png)

Step 2: I needed to select the TXT record which holds any TXT data such as verification/security related data of website.thm which I received the flag

![Alt text for the image](/Screenshots/TXT.png)

Step 3: I recieved the MX record which holds the mail servers responsible for sending mails on the behalf of the domain for website.thm

![Alt text for the image](/Screenshots/MX.png)

Step 4: I retrieved the A record which holds the hostnames translated to IPv4 addresses

![Alt text for the image](/Screenshots/A.png)

In these sections, I made basic HTTP requests such:

In this one I made a GET request and received the response. I selected GET and then the particular page I needed which was `/room`
![Alt text for the image](/Screenshots/GET.png)

In this one I made a GET request and received the response. I selected GET and then the particular page I needed which was `/blog` but with the id set to 1
![Alt text for the image](/Screenshots/GET_2.png)

This one was a simple DELETE a particular user which was user 1
![Alt text for the image](/Screenshots/DELETE.png)

Here I needed to create/update a new user which was user 2
![Alt text for the image](/Screenshots/PUT.png)

This was the last one in which I needed to set two parameters of username to thm and password to letmein and make a POST request (creating a resource) to retrieve the flag
![Alt text for the image](/Screenshots/POST.png)

Finally, we have the whole idea of getting a website to display on your page in these two images

You first type in tryhackme.com into your browser and then it checks its local cache. If not found, request forwarded to the recursive DNS server which also has a local cache. If it is not found there, your request is redirected to the root DNS server which returns the correct TLD server (such as .com TLD server or tryhackme.com). The TLD server then responds with the correct authoritative DNS server which usually has the answer to your DNS request. It sends a local copy to the recursive DNS server. Next, once your browser has the IP address, it makes a TCP connection (port 80 or 443 for HTTP/HTTPS) to the web server. It then makes a GET request to the web server but first that passes may pass through a WAF to make sure your request is real.

![Alt text for the image](/Screenshots/Website_Part1.png)

We continue here in which your request may pass through the WAF to a load balancer and the LB sends your request to the least busy server. The web server receives your GET request, searches its database, and then sends it back from the port --> LB --> WAF --> and your browser registers it on your screen.

![Alt text for the image](/Screenshots/Website_Part2.png)


### Key Learning Points

* DNS converts domain names into IP addresses so browsers can locate servers.
* DNS resolution involves recursive, root, TLD, and authoritative servers.
* Modern websites rely on infrastructure such as **WAFs, load balancers, web servers, and databases** to handle traffic and deliver content efficiently.
* Understanding this flow is important in cybersecurity because attackers often target weak points in the web request process.
