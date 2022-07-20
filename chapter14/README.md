# Chapter 14 Application Security

[dlint](https://github.com/duo-labs/dlint) - Static python code testing tool  
[Cybersecurity Framework](https://www.nist.gov/cyberframework/online-learning/components-framework) - NIST.gov  
[OWASP Top 10](https://owasp.org/www-project-top-ten/) - OWASP Top Ten  
[U.S. National Vulnerability Database NVD](https://nvd.nist.gov/) - National Vulnerability database  
[CERT/CC Vulnerability Notes Database](https://www.kb.cert.org/vuls/) - CERT vulnerability Notes  


## Identifying Potential Risks 

The National Institute of Standards and Technology (NIST) defines a framework called the Cybersecurity Framework that is shown in Figure 14-1 . The framework organizes necessary cybersecurity activities into the following functions:  

* **Identify:** An organization needs to understand what kinds of cybersecurity risks can affect daily modes of operation. Areas such as data theft, network breaches, and employee information are some of the risks that need to be identified.  
* **Protect:** An organization needs to understand what it can do to prevent attacks. Protection could include deploying proper networking elements such as firewalls and tools for better software development. Protection helps minimize the impact of any attack.  
* **Detect:** It is important to install tools that detect any data breaches or attacks in a time-sensitive manner or while attacks are happening.  
* **Respond:** An organization needs to have a plan in place to deal with an attack. It needs to know what procedures need to be followed and what can be done to minimize the impact of an attack.  
* **Recover:** An organization needs to be able to quickly resolve any services or systems that have been affected. 

For more details visit [Cybersecurity Framework](https://www.nist.gov/cyberframework/online-learning/components-framework) 

(Kindle Locations 10171-10181). 

## Common Threats and Mitigations 

Before we talk about the potential risks, it is essential to understand some key terms and their relationships. The following are some commonly misunderstood terms:  

* **Asset:** An asset is something you’re trying to protect. It could be information, data, people, or physical property. Assets are of two types: tangible and intangible. Information and data may include databases, software code, and critical company records. People include employees and customers. Intangible assets include reputation and proprietary information.  
* **Threat:** Anything you are trying to protect against is known as a threat. A threat is any code or person that can exploit a vulnerability when it has access to an asset and can control or damage the asset. Vulnerability: A vulnerability is a weakness or gap in protection efforts. It can be exploited by threats to gain unauthorized access to an asset.  
* **Risk:** Risk is the intersection of assets, threats, and vulnerabilities. Certain risks can potentially compensate for loss, damage, or destruction of an asset as a result of a threat exploiting a vulnerability. Threats can always exist, but if vulnerabilities don’t exist, then there is little or no risk. Similarly, you can have a weakness, but if you have no threat, then you have little or no risk.  
(Kindle Locations 10188-10198). 

### Common Threats and Mitigations  

* Buffer Overflow  
  * Separate executable memory from non-executable memory.  
  * Randomize address spaces for data.  
  * Use the built-in protection options in newer software OSs and languages. 
* Man in the Middle  
  * Adopt a Secure Sockets Layer (SSL)/Transport Layer Security (TLS) strategy for both web and email.  
  * Avoid sensitive data in public Wi-Fi or computers.  
* DoS, DDOS
  * Use specially designed protection services (cloud or network). 
* XSS
  * Validate and sanitze input data  
  * Employ cookie security, such as timeouts, encoding the client IP address, and so on. 
* Phising
  * Educate users to avoid falling for the bait.  
  * Detect and mark emails and sites as spam. 
* Malware
  * Deploy technologies that continually monitor and detect malware that has evaded perimeter defenses. 
* SQLi
  * Use character escaping.  
  * Use stored procedures as opposed to queries.Enforce privileges. 
* Brute Force  
  * Lock the system after a specified number of attempts.  
  * Use two-factor authorization.  

</br>


OWASP has defined a list of security risks called the [OWASP Top 10](https://owasp.org/www-project-top-ten/)  
This is the current OWASP Top 10 list:  

* **Injection**
* **Broken authentication**  
* **Sensitive data exposure**  
* **XML external entities** 
* **Broken access control**  
* **Security misconfiguration**  
* **Cross-site scripting**  
* **Insecure deserialization** 
* **Using components with known vulnerabilities**  
* **Insufficient logging and monitoring** 
(Kindle Locations 10253-10255)  


**CVE** - Common Vulnerabilities and Exposures  
CVEs are supervised by the MITRE Corporation, with funding from the Cybersecurity and Infrastructure Security Agency, part of the U.S. Department of Homeland Security.  

A CVE record usually provides a short one-line description. Details are usually available on sites such the [U.S. National Vulnerability Database NVD](https://nvd.nist.gov/) and the [CERT/CC Vulnerability Notes Database](https://www.kb.cert.org/vuls/)  

### CVE Detection Using Nmap  
One of Nmap’s most magnificent features for finding vulnerabilities is called the Nmap Scripting Engine (NSE). The NSE allows you to use a predefined script or even write your own by using Lua programming language. Using NSE is a crucial part of automating system and vulnerability scans. It requires the following syntax:  
**nmap -Pn --script vuln hostname**  
(Kindle Locations 10307-10311).  


###Tiers of Securing and Protecting  

To minimize risks, the following are some of the best practices in the industry:  

* **Keep software up-to-date:** Install software patches so that attackers cannot take advantage of known problems or vulnerabilities. Many operating systems offer automatic updates.  
*  **Install end-user or device security:** Install endpoint security software on an end user’s device so that viruses and malware are kept as far away as possible.  
*  **Use strong passwords:** Using a strong password ensures that only authorized users can access resources. With strong passwords, it becomes hard to guess and hence decreases security risk.  
*  **Implement multifactor authentication (MFA):** Authentication is a process used to validate a user’s identity. Attackers commonly exploit weak authentication processes. MFA uses at least two identity components to authenticate a user’s identity, minimizing the risk of a cyberattacker gaining access to an account by knowing the username and password.  
*  **Install a firewall:** Firewalls may be able to prevent some types of attack vectors by blocking malicious traffic before it can enter a computer system and by restricting unnecessary outbound communications.  
*  **Encrypt data:** Ensure that data cannot be accessed even if storage can be reached.  
(Kindle Locations 10375-10376).  

### Data Security Types  

* **Data in Motion**  
* **Data at Rest**  
* **Data in use (Memory)**  

###Secure Development Methods 

As mentioned earlier in this chapter, the application security process starts during the development phase. Instead of trying to bring in security at the end of the development process, secure development needs to be baked in from the start. Addressing security issues from the very beginning saves a company time and money in the long run.  

It is a common practice for corporations to use some type of software development lifecycle (SDLC). Best practices in secure software development suggest integrating security aspects into each phase of the SDLC. Figure 14-6 show the various aspects of the SDLC. 

(Kindle Locations 10443-10448).  

<p align="left" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter14/images/ch14-SecureDevelopment.png"> 
</p>  



The SDLC includes these steps:  

* **Training:** Training helps get everyone on the project teams into a security frame of mind. Teach and train developers on the team to analyze the business application attack surface as well as the associated potential threats. Not just developers but all team members should understand the exposure points of their applications (user inputs, front-facing code, exposed function calls, and so on) and take steps to design more secure systems wherever possible.  
* **Threat modeling:** For every component and module in a system, ask the “what-how-what” questions: What can go wrong? How can someone try to hack into it? What can we do to prevent this from happening? Various frameworks for threat modeling are available, including the following: 

  * STRIDE (Spoofing, Tampering, Repudiation, Information Leak, DoS, Elevation of Privilege) 
  * PASTA (Process for Attack Simulation and Threat Analysis)  
  * VAST (Visual, Agile, and Simple Threat Modeling)  
* **Secure coding:** Build and use code libraries that are already secured or approved by an official committee. The industry has several guidelines for secure coding, and we have listed some of the standard ones here:   
  * Validating inputs  
  * Encoding output  
  * Ensuring authentication and credential management  
  * Managing sessions  
  * Using access control lists  
  * Monitoring error handling and logging  
  * Protecting data, including files, databases, and memory  
	
* **Code review:** Code review is one of the most essential steps in securing an application. Usually, the rule that you have to keep in mind is that pen testing and other forms of testing should not be discovering new vulnerabilities. Code review has to be a way to make sure that an application is self-defending. Also, it should be conducted using a combination of tools and human effort. It is important to designate a security lead who can help review code from a security point of view.  
* Secure tooling: Static analysis helps catch vulnerabilities. Static analysis tools detect errors or potential errors in the structure of a program and can be useful for documentation or understanding a program. Static analysis is a very cost-effective way of discovering errors. Data flow analysis is a form of static analysis that concentrates on the use of data by programs and detects some data flow anomalies.  
  * [Dlint](https://github.com/duo-labs/dlint) is a tool from Duo Labs (Cisco) that defines and checks for common best practices when it comes to writing secure Python. To evaluate a variety of rules over a code base, Dlint leverages Flake8. Flake8 does the heavy lifting of parsing Python’s AST, allowing you to focus on writing robust rule sets.  
* **Testing:**  Testing includes penetration testing and system testing, black box testing, and white box testing. Black box testing is a method used to test software without knowing the internal structure of the code or program. Testing teams usually do this type of testing, and programming knowledge is not required. Black box testing includes functional testing, behavior testing, and closed box testing. White box testing, on the other hand, is a software testing method in which internal structure is known to the tester who is testing the software. Generally, this type of testing is carried out by software developers. Programming knowledge is usually required for white box testing. White box testing includes structural testing, logic testing, path testing, loop testing, code coverage testing, and open box testing.  

Testing involves the following steps:  

* **Intelligence gathering:** Define the goals, understand what’s included in the application, and identify potential areas of vulnerabilities.  
* **Scanning:** Understand both running and non-running behaviors. Static analysis tools enable developers and testers to see faults without actually running an application. These tools can save a lot of time and effort in the long run, and the more errors and defects found here, the better. Dynamic analysis, on the other hand, involves actually running the application in a real or virtual environment. Usually, a lot of external services and interactions are exercised here.  
* **Access:** Use various methods to try to hack the application, such as testing the app for SQL injection, back doors, traffic interception, and so on. Long-term access testing looks at the kinds of vulnerabilities exposed when a system is exploited for a long time.  
* **Reporting:** Include all details on the vulnerabilities and sensitive data exposed, as well as the amount of time the system remained unhacked. 
(Kindle Locations 10488-10489).  


### Load balancing uses algorithms such as the following:  
* **Round-robin:** Selects servers in turn 
* **Least connected:** Selects the server with the lowest number of connections; this is recommended for more extended sessions  
* **Source/IP-hash:** Chooses a server based on a hash of the source IP 
* **Cookie marking:** Adds a field in the HTTP cookies, which could be used for decision making  
* **Consistent IP-hash:** Adds and removes servers without alarming cached items or session persistence 
(Kindle Locations 10599-10600). 

### Reverse Proxy  
A reverse proxy accepts a request from a user, forwards it to a server that can fulfill it, and returns the server’s response to the client. A reverse proxy can include some or all of the following functionality:  

* **Security:** The web servers or application servers are not visible from the external network, so malicious clients cannot access them directly to exploit any vulnerabilities. Many reverse proxy servers include features that help protect backend servers from distributed denial-of-service (DDoS) attacks—for example, by rejecting traffic from particular client IP addresses (blacklisting) or limiting the number of connections accepted from each client.  
* **Scalability and flexibility:** Clients see only the reverse proxy’s IP address. This is particularly useful in a load-balanced environment, where you can scale the number of servers up and down to match fluctuations in traffic volume.  
* **Web acceleration:** Acceleration in this case means reducing the time it takes to generate a response and return it to the client. Some of the techniques for web acceleration include the following: 
  * **Compression:** Compressing server responses before returning them to the client (for instance, with gzip) reduces the amount of bandwidth they require, which speeds their transit over the network.  
  * **SSL termination:** Encrypting the traffic between clients and servers protects it as it crosses a public network such as the Internet. However, decryption and encryption can be computationally expensive. By decrypting incoming requests and encrypting server responses, the reverse proxy frees up resources on backend servers, which the servers can then devote to their primary purpose—serving content.  
  * **Caching:** Before returning the backend server’s response to the client, the reverse proxy stores a copy of it locally. When the client (or any other client) makes the same request, the reverse proxy can provide the response itself from the cache instead of forwarding the request to the backend server. This both decreases response time to the client and reduces the load on the backend server. This works great for “static” content, but there are new techniques that can be used for “dynamic” content as well.  
* **Content filtering:** This involves monitoring traffic to and from the web server for potentially sensitive or inappropriate data and taking action as necessary.  
* **Authentication:** The reverse proxy authenticates users via a variety of mechanisms and controls access to URLs hosted on the web server. 
(Kindle Locations 10620-10621). 

<p align="left" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter14/images/ch14-Reverse-Proxy.png"> 
</p>  

Figure 14-15 illustrates the concept of a reverse proxy with a user requesting a web page from https://server.com . In this case, server.com is the reverse proxy, which first terminates SSL and then translates the request and issues a new request to the images.server.com server. The images server then responds to the request, gathering and translating the response and sending it back to the client. The translation could mean applying compression (gzip) to the response. 

<p align="left" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter14/images/ch14-Reverse-Proxy-Flow.png"> 
</p> 

## Rewiew All Key Topics  
List - Assets, Threats, vulnerabilities, and risks - Location 10186  
Table 14.2 - Threats and mitigations - Location 10186  
Paragraph - Open Web Applicaiton Security Project - Location 10245  
Figure 14.5 - Data Security - Location 10411
Paragraph - Firewalls - Location 10490  
Paragraph - Intrusion Detection Systems - Location 10522  
Paragraph - Domain Name System - Location 10538  
List - Reverse Proxy - Location 10594  

