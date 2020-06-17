#installing tldextract
pip install tldextract

#importing tldextract
import tldextract

#declaring the list of subdomains
subdomain = ["p2pprod.domain.com","p2pprod.domain2.com","p2pprod.domain3.com","p2pprod.domain4.com","p2pprod.domain5.com"]

# now lets convert subdomain to domain
domain = []
for i in subdomain:
  value = tldextract.extract(i)
  domain.append(value.domain+"."+value.suffix)

# Now lets convert them to csv
import csv
from google.colab import files
domaininfowrite = open('domaininfotoday2.csv','w',newline='')
writer = csv.writer(domaininfowrite,lineterminator='\n')
writer.writerow(['subdomain','domain'])
for i in range(len(domain)):
  writer.writerow([subdomain[i],domain[i]])

ls

files.download('/content/domaininfotoday2.csv')
