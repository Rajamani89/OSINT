import requests
import json,csv
# importing the source data of ipaddress
ipinfo = ["103.18.108.129",
"109.74.157.200",
"109.74.157.53",
"120.150.207.13",
"139.162.222.202"]
# next step is forming the url
vturl = []
for i in ipinfo:
  vturl.append("https://www.virustotal.com/api/v3/ip_addresses/"+i+"/historical_whois")

import time
#to slow down my request
domaininfowrite = open('ipinfo5.csv','w',newline='')
writer = csv.writer(domaininfowrite,lineterminator='\n')
writer.writerow(['vturl','registrant_country','whois_map','CIDR','NetName','NetRange',])
# step 4 send all url in as a request
#writing them during the request itself
querystring = {"limit":"10"}
headers = {'x-apikey':'enter your key'}

cidr = []
NetName = []
NetRange = []
NetType = []
OrgTechEmail = []
OrgTechName = []
Organization = []
OrgName = []
count = 0
for i in vturl:
  response = requests.request("GET",i, headers=headers, params=querystring)
  count = count + 1
  print(count)
  output = json.loads(response.text.encode('utf8'))
  time.sleep(5)
  if output['data'] == []:
    cidr.append("none found")
    NetName.append("none found")
    NetRange.append("none found")
    NetType.append("none found")
    OrgTechEmail.append("none found")
    OrgTechName.append("none found")
    Organization.append("none found")
    OrgName.append("none found")
  else:
    try:
  	  cidr.append(output['data'][0]['attributes']['whois_map']['CIDR'])

    except KeyError:
  	  cidr.append("none found")
  	  print(i,"none found cidr")

    try:
  	  NetName.append(output['data'][0]['attributes']['whois_map']['NetName'])
    except KeyError:
  	  NetName.append("none found")
  	  print(i,"none found netname")

    try:
  	  NetRange.append(output['data'][0]['attributes']['whois_map']['NetRange'])
    except KeyError:  	
  	  NetRange.append("none found")
  	  print(i,"none found NetRange")

    try:
  	  NetType.append(output['data'][0]['attributes']['whois_map']['NetType'])
    except KeyError:
  	  NetType.append("none found")
  	  print(i,"none found NetType")

    try:
  	  OrgTechEmail.append(output['data'][0]['attributes']['whois_map']['OrgTechEmail'])
    except KeyError:
  	  OrgTechEmail.append("none found")
  	  print(i,"none found orgtechemail")

    try:
  	  OrgTechName.append(output['data'][0]['attributes']['whois_map']['OrgTechName'])
    except KeyError:
  	  OrgTechName.append("none found")
  	  print(i,"none found OrgTechName")

    try:
  	  Organization.append(output['data'][0]['attributes']['whois_map']['Organization'])
    except KeyError:
  	  Organization.append("none found")
  	  print(i,"none found Organization")

    try:
  	  OrgName.append(output['data'][0]['attributes']['whois_map']['OrgName'])
    except KeyError:
  	  OrgName.append("none found")
  	  print(i,"none found OrgName")
	
    time.sleep(9)
	
  
  print(i)
for y in range(len(vturl)):
	writer.writerow([vturl[y],cidr[y],NetName[y],NetRange[y],OrgTechEmail[y],OrgTechName[y],Organization[y],OrgName[y]])
	time.sleep(5)
    
from google.colab import files
files.download('/content/ipinfo4.csv')
