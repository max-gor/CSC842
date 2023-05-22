# CSC842-Summer 2023
This repository includes projects for CSC 842 Security Tool Development course.

**Tool1
Home Network Scanner**

I was always interested in IoT security. Home wireless routers often do not have ways to check for all the devices connected to the network. Wireless routers also do not have tools that scan connected devices for vulnerabilities. This Home Network Scanner Python program scans the network for devices and identifies their IP addresses, MAC addresses, and vendor (if available). The main configuration of the tool runs a single scan, provides output with the device information, saves connected devices’ IP addresses to a file, runs the Nmap vulnerability assessment script against the list of the addresses, and saves the result to another text file.

**Three main ideas:**
1.	IoT devices always lack security since they run in the background and do the job, while users do not have adequate interfaces to scan the devices for vulnerabilities.
2.	Python is one of the best languages to work with networking tools.
3.	Nmap is a simple, open-source utility that can be used for such functions as network enumeration or vulnerability scanning.

**Limitations and future work**
Due to the limited amount of time to work on the tool, I have not been able to work on vulnerability fixes for the identified vulnerabilities. This project would also benefit from attempting to install the program on the router, which I have not attempted either. These options could be addressed during future attempts to work on the projects.

**Running the program**
If you are planning to run the code, you can download it from the GitHub repository. You need to make sure you have python-nmap libraries installed, and you run the program as a root since included Nmap modules require privilege escalation. You can convert the program to an ongoing scanner by uncommenting all the lines that begin with “#*.” Happy scanning!
