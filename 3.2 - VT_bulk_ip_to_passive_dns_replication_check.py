
import requests
import json,csv
# importing the source data of ipaddress
ipinfo = ["104.167.11.239",
"104.196.179.79",
"107.180.39.226",
"107.180.4.121"]
# next step is forming the url
vturl = []
for i in ipinfo:
  vturl.append("https://www.virustotal.com/api/v3/ip_addresses/"+i+"/resolutions")

#writing the firstline in the csv
domaininfowrite = open('ipinfo2.csv','w',newline='')
writer = csv.writer(domaininfowrite,lineterminator='\n')
writer.writerow(['totalpassivednsdomain','domain'])
# step 4 send all url in as a request
#writing them during the request itself
querystring = {"limit":"10"}
headers = {'x-apikey': 'API'}
for i in vturl:
  response = requests.request("GET",i, headers=headers, params=querystring)
  output = json.loads(response.text.encode('utf8'))
  for y in range(len(output['data'])):
    writer.writerow([i,output['data'][y]['attributes']['host_name'],str(len(output['data']))])

from google.colab import files
files.download('/content/ipinfo2.csv')
