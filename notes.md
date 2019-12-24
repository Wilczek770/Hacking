6:16:42

Tools:
* The harvester 
    * find emails, subdomains etc. 
    * https://github.com/laramies/theHarvester
* Bluto
    * pip install bluto
    * scan HaveI_beenPwned or sth 
    * https://github.com/darryllane/Bluto [?]
* crt.sh 
    * certificates for subdomain scanning
* wappalyzer 
    * chrome / ff extension 
    * analyze technologies used on a website
* whatweb 
    * actively scan website
* https://builtwith.com/ 
    * explore used technologies 


=== === === === === === === ===

# Scanning
* scanning -> usually on TCP side, but sometimes UDP is also important
* TCP
    * Has a handshake
    * High-reliability applications
    * HTTP, FTP, Telnet
* UDP
    * No handshake
    * DNS, DHCP, SNMP
* Three - way handshake
    * ACK -> [SYN, ACK] -> ACK (Hello)
* NMap
    * Stealth scan:
        * SYN -> [SYN, ACK] -> RST (reset)
    * nmap -sn 192.168.0.0/16
    * nmap -T4 192.168.0.1 <- search for open ports on ip
    * nmap scripts
* Nessus home
    *
    