
# # Pulling CVE information from NVD per month

# ### Requesting to nvd URL parsing the results in beautifull SOUP

import requests
import re
from bs4 import BeautifulSoup
page = "https://nvd.nist.gov/vuln/full-listing/2019/11"
result = requests.get(page)
resulttext = result.text
soup = BeautifulSoup(result.text,'html.parser')

# ### Converting the CVE position into list if you use .text method that will be string

scraplist = list(soup.find_all('span',class_='col-md-2',attrs='href'))

# ### Now you can use the CSV writer to input them in a csv file
import csv

writefile = open('nvd.csv','w',newline='')
writer = csv.writer(writefile)
writer.writerow(['cve name'])
for i in range(len(scraplist)):
    writer.writerow([scraplist[i].text])
writefile.close()

#URL CONSTRUCTION
# general URL format of NVD
# https://nvd.nist.gov/vuln/detail/CVE-2019-13307
nvdurl = "https://nvd.nist.gov/vuln/detail/"
nvdurllist = []
for i in range(len(scraplist)):
    fullnvdurl = nvdurl+scraplist[i].text
    #There is one extra space 'https://nvd.nist.gov/vuln/detail/ CVE-2005-2350'
    fullnvdurl = fullnvdurl.replace('/ CVE','/CVE')
    nvdurllist.append(fullnvdurl)

#This part is work in progress
import time
def foo():
  print(time.ctime())
for i in range(len(nvdurllist)):
    foo()
    # HERE you have to code the cve information fill part
    time.sleep(10)
    # to delay the request
