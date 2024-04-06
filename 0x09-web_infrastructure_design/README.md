0x09. Web infrastructure design
===

This document summarizes three web infrastructure designs for the website www.foobar.com, highlighting their components and potential issues, incorporating the clarifications you provided.

Task 1: One-Server Web Infrastructure
===

Components:
---

User: Initiates web requests.  
Internet: Connects users to the server.  
Server (with Nginx, Application Server, Codebase, and MySQL Database):  
Nginx (Web Server): Serves static content and interacts with the database (if needed).  
Application Server: Processes application logic and interacts with the database.  
Codebase: Stores your application code.  
MySQL Database: Stores website data.  
DNS Server (External): Resolves domain names to IP addresses (not shown explicitly).  

Issues:
---

Single Point of Failure (SPOF): The server is a SPOF. If it fails, the entire website becomes unavailable.  
No Security: No firewalls or HTTPS encryption are implemented, making the website vulnerable to attacks and insecure data transmission.  
No Monitoring: No monitoring tools are in place to identify potential issues proactively.  

Task 2: Three-Server Web Infrastructure (Initial Design)
===

Components:
---

User: Initiates web requests.  
Internet: Connects users to the Load Balancer.  
Load Balancer (HAproxy): Distributes traffic across web and application servers.  
Server 1 (Web Server & Application Server):  
Nginx (Web Server): Serves static content (potentially interacts with the database).  
Application Server: Processes application logic and interacts with the database.  
Codebase: Stores your application code.  
Primary MySQL Database: Stores website data.  
Server 2 (Web Server & Application Server):  
Nginx (Web Server): Serves static content (potentially interacts with the database).  
Application Server: Processes application logic and interacts with the database replica.  
Codebase: Stores your application code.  
Replica MySQL Database: Synchronized copy of the primary database.  

Issues:
---
SPOF: The Load Balancer is a SPOF. If it fails, no traffic reaches the web or application servers.  
Limited Redundancy: While a database replica exists, the primary database server remains a SPOF for writes.  

Task 3: Three-Server Web Infrastructure (Secure and Monitored Design)
===

Components:
---

User: Initiates web requests.  
Internet: Connects users to the firewall.  
3 Firewalls: Filter incoming and outgoing traffic on each server (Load Balancer, Web Servers).  
Load Balancer (HAproxy with SSL Termination): Distributes traffic and terminates HTTPS connections.  
Web Server 1 (Nginx): Serves static content and interacts with the database (if needed).  
Codebase: Stores your application code.  
Monitoring Client (Sumologic): Collects server performance data.  
Web Server 2 (Nginx): Serves static content and interacts with the database replica (if needed).  
Codebase: Stores your application code.  
Monitoring Client (Sumologic): Collects server performance data.  
Database Server (MySQL Primary): Stores website data.  
Monitoring Client (Sumologic): Collects database performance data.  
Database Server Replica (MySQL): Synchronized copy of the primary database.  

Issues:
---

Potential Issue: Terminating SSL at the Load Balancer can make decryption keys more vulnerable. Consider web server termination for better security.  
Limited Scalability in the Long Run: Running all components (web server, application server, database) on both web servers might be inefficient for handling significant growth. Consider separation of concerns for better scalability.  

Additional Notes:
---

These designs provide a basic understanding of web infrastructure concepts. Real-world deployments might involve additional components and configurations.  
Security is paramount. Always implement firewalls, HTTPS, and intrusion detection/prevention systems for robust protection.  
Monitoring is crucial for proactive problem identification and website health maintenance.  
