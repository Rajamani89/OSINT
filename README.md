# Cyber security information gathering
This repositories contain multiple cyber securtiy information gathering techniques
## CVE information gathering
### 1 - Gathering all the CVE released from NVD
![picture](https://nvd.nist.gov/NVD/Media/images/favicons/apple-touch-icon.png)

The NVD is the U.S. government repository of standards based vulnerability management data represented using the Security Content Automation Protocol (SCAP)
Its the best place to have uptodate information about what CVE is released on which day.
Advantage of NVD is it have high coverage of all the CVE released
This repositories have documentation of how to gather CVE and its info from NVD

#### 1.1- Scraping CVE information from NVD this month and URL contruction.ipynb

#### 1.2 - NVD zip Feeds.py 

#### 1.3 - nvdwebextract.py USING SCRAPY

#### 1.4 - nvdwebextract using beautifull soup find all function

### 2 - IBM Xforce CVE CHECK python
![picture](https://www.cisco.com/c/dam/m/en_us/products/security/technical-alliance-partners/core/img/partners/ibm-security.png)

Contain the code for how to extract cve details from IBM and storing in a CSV file,which can be later utilised for further analytics and operation

#### 2.1 - IBM XFORCE CVE CHECK.py

### 3 - VIRUS TOTAL
![picture](https://www.virustotal.com/gui/images/manifest/icon-192x192.png)

#### 3.1 - SCRAPING FROM VT WITHOUT USING API.py
#### 3.2 - for downloading passive dns entries for all the ip address using API
#### 3.3 - for downloading whois using VT api

### 4 - URLSCAN.IO
![picture](https://urlscan.io/img/urlscan_256.png)

#### 4.1 - URLSCAN-searchapi.py
### 5 - Alien vault
![picture](https://cdn5.alienvault.com/images/uploads/AV.Logo.CertifiedSE.PMS-2_copy.jpg)


contain code inorder query Alienvault for any campaign


### 6 - robtext
contain codes for the bulk checking of domain for name server , ip address , mail server

### 7 - subdomain manupulation
Contain code to convert subdomains to domain using tldextract

### 8 - shodan search
Use shodan search api

## 9 -  FOFA Search
Use of FOFA API
