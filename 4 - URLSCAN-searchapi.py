import requests
import json
import csv

url = "https://urlscan.io/api/v1/search/?q=domain:rcam.target.com"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
#converting to dict
respdict = json.loads(response.text.encode('utf8'))
size = len(respdict["results"])
writefile = open('c:\\users\\path\\path\\Desktop\\urlscan.csv','w',newline = '')
writer = csv.writer (writefile)

writer.writerow(['visibility','method','time','source','url','country','server','domain','ip','asnname','result'])
for i in range(size):
    print(i)
    writer.writerow([str(respdict["results"][i]['task']['visibility']),str(respdict["results"][i]['task']['method']),str(respdict["results"][i]['task']['time']),str(respdict["results"][i]['task']["source"]),str(respdict["results"][i]['task']["url"]),str(respdict["results"][i]["page"]["country"]),str(respdict["results"][i]["page"]["server"]),str(respdict["results"][i]["page"]["domain"]),str(respdict["results"][i]["page"]["ip"]),str(respdict["results"][i]["page"]["asnname"]),str(respdict["results"][i]["result"])])
   
writefile.close()
