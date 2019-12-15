#!/usr/bin/env python
# coding: utf-8

# In[154]:


import requests
from bs4 import BeautifulSoup
from pprint import pprint
import webbrowser
from lxml import etree
import os



response =  requests.get('https://nvd.nist.gov/vuln/detail/CVE-2019-13307')


# not required
#soup = BeautifulSoup(responsetext,'xml')
#responsetext = response.text



#writing the file in local system
writehtml = open('response.html','w',newline='')
writehtml.write(response.text)
# parsing with etree
htmlparser = etree.HTMLParser()
tree = etree.parse('response.html',htmlparser)
# using xpath to pull info
score = tree.xpath('/html/body/form/div[3]/div[1]/div/table//tr/td/div/div[1]/div[2]/div[2]/div/div[2]/span/span/a/text()')
description = tree.xpath('/html/body/form/div[3]/div[1]/div/table//tr/td/div/div[1]/p[1]/text()')
vector = tree.xpath('/html/body/form/div[3]/div[1]/div/table//tr/td/div/div[1]/div[2]/div[2]/div/div[3]/span/span/text()')





