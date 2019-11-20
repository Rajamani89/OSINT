#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
import zipfile
import csv
import json
page = "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2019.json.zip"
result = requests.get(page)


# In[8]:


import io
zipout = zipfile.ZipFile(io.BytesIO(result.content))


# In[9]:


zipout.extractall()


# In[30]:


nvdjson = open("nvdcve-1.1-2019.json")


# In[31]:


nvddict = json.load(nvdjson)


# In[40]:


nvddict['CVE_Items'][0]


# In[ ]:




