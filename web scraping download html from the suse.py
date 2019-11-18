#!/usr/bin/env python
# coding: utf-8

# In[66]:


import requests
from bs4 import BeautifulSoup
page = "https://www.suse.com/pt-br/security/cve/CVE-2019-13307"
result = requests.get(page)
resulttext = result.text
soup = BeautifulSoup(result.text,'html.parser')


# In[67]:


with open ('SUSE.html','w',encoding='utf-8') as redhathtml:
    redhathtml.write(resulttext)


# In[133]:


soup.body.td.next_element.next_element.next_element.text


# In[128]:


tabledata


# In[137]:


soup.select ('body > main > div.container-fluid.support-document.cve > div > div > table:nth-child(10) > tbody > tr:nth-child(3) > td:nth-child(3)')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




