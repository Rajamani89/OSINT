"""
Created on Sat Nov  2 23:57:25 2019

@author: rajamani
"""
#Importing the required module
import requests,json,csv
# This cve list can be taken as input by reading a file also in this example i just manually added
#this list will be looped
cvelist = ['CVE-2019-13721','CVE-2019-18230'] 
#API URL
baseurl = "https://api.xforce.ibmcloud.com/vulnerabilities/search/"
# no payload
payload = {}
headers = {
  'Authorization': 'Basic KEY'
}
url = ""
count = 0
resplist=[]
#Making API calls for all cve
for i in cvelist:
    url = baseurl + i
    response = requests.request("GET", url, headers=headers, data = payload)
   # print(response.text.encode('utf8')) 
   #also working# jsonvalue = json.loads(response.text.encode('utf8'))
   
 #Converting to python value
    pvalue = json.loads(response.text)
    print(type(pvalue),"created")
    print(pvalue)
    print("\n #########break#########\n")  
 #Appending all the queries made in a master list resplist
    resplist.append(pvalue)

# Now you can think of saving in a CSV file am not using append because every time this program run the file should be new
cvewrite = open('cvetoday.csv','w',newline='')
writer = csv.writer(cvewrite,lineterminator='\n')
writer.writerow(['CVE','TITLE','DESCRIPTION','CVSS','IBMURL'])
# Now iterate the values in the master CVE response list and write on the next line
for i in range(len(resplist)): 
	print("\n #########writing CSV file#########","count ",count,".\n")
	writer.writerow([str(resplist[i][0]['stdcode']),resplist[i][0]['title'],resplist[i][0]['description'],str(resplist[i][0]['risk_level']),str(resplist[i][0]['xfdbid'])])
	count = count + 1
    
 #xfdbid can be used to determine the IBM url by concatenating with "https://exchange.xforce.ibmcloud.com/vulnerabilities/" and remember to convert to string
cvewrite.close()

#If you are running this in google colab environment
#check file path using pwd command
from google.colab import files
files.download('/content/cvetoday.csv')
