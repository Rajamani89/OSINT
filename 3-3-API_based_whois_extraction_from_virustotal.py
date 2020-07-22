import requests
import json,csv
# importing the source data of ipaddress
ipinfo = ["161.135.105.139","161.135.105.140","204.135.9.10"]
# next step is forming the url
vturl = []
for i in ipinfo:
  vturl.append("https://www.virustotal.com/api/v3/ip_addresses/"+i+"/historical_whois")

import time
#to slow down my request
domaininfowrite = open('fedex4.csv','w',newline='')
writer = csv.writer(domaininfowrite,lineterminator='\n')
writer.writerow(['vturl','registrant_country','whois_map','CIDR','NetName','NetRange',])
# step 4 send all url in as a request
#writing them during the request itself
querystring = {"limit":"10"}
headers = {'x-apikey':'put your key here'}
for i in vturl:
  response = requests.request("GET",i, headers=headers, params=querystring)
  output = json.loads(response.text.encode('utf8'))
  for y in range(len(output['data'])):
    writer.writerow([i,output['data'][y]['attributes']['registrant_country'],output['data'][y]['attributes']['whois_map']['Address'],output['data'][y]['attributes']['whois_map']['CIDR'],output['data'][y]['attributes']['whois_map']['NetName'],output['data'][y]['attributes']['whois_map']['NetRange'],output['data'][y]['attributes']['whois_map']['NetType'],output['data'][y]['attributes']['whois_map']['OrgTechEmail'],output['data'][y]['attributes']['whois_map']['OrgTechName'],output['data'][y]['attributes']['whois_map']['Organization'],output['data'][y]['attributes']['whois_map']['OrgName']])
    time.sleep(4)
