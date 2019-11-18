
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

