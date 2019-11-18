#!/usr/bin/env python
# coding: utf-8

# # Pulling CVE information from NVD per month

# In[24]:


import requests
import re
from bs4 import BeautifulSoup
page = "https://nvd.nist.gov/vuln/full-listing/2019/11"
result = requests.get(page)
resulttext = result.text
soup = BeautifulSoup(result.text,'html.parser')


# ### Requesting to nvd URL parsing the results in beautifull SOUP

# In[25]:


scraplist = list(soup.find_all('span',class_='col-md-2',attrs='href'))


# ### Converting the CVE position into list if you use .text method that will be string

# In[34]:


import csv


# In[35]:


writefile = open('nvd.csv','w',newline='')
writer = csv.writer(writefile)
writer.writerow(['cve name'])
for i in range(len(scraplist)):
    writer.writerow([scraplist[i].text])
writefile.close()


# ### Now you can use the CSV writer to input them in a csv file

# In[ ]:




