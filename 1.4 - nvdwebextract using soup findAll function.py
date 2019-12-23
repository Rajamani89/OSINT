# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
#Using soup
html =  requests.get("https://nvd.nist.gov/vuln/detail/CVE-2019-13307")
bs = BeautifulSoup(html.text,'html.parser')
#Pull description
description = bs.findAll('p',attrs={'data-testid':'vuln-description'})
descriptiontext = description[0].get_text()
#Pull vector info
vector = bs.findAll('span',attrs={'class':'tooltipCvss3NistMetrics'})
vectortext = vector[0].get_text()
#pull score information
score = bs.findAll('a',attrs={'id':'p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_zoneCenter_VulnerabilityDetail_VulnFormView_Cvss3NistCalculatorAnchor'})
scoretext = score[0].get_text()



