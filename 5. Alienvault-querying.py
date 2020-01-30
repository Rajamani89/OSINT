import csv
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes

otx = OTXv2("YOUR API")
# querying alienvault
pulsesresult = otx.search_pulses("tag:ransomware", max_results=2000)
#create csv
ransomwrite = open('ransomtoday.csv','w',newline='')
writer = csv.writer(ransomwrite,lineterminator='\n')
# making the cloumn names
writer.writerow(['Authorname','created','description','industries','malware_families','name','references','tags','targeted_countries'])

# Now iterate the values in the master ransom response list and write on the next line

count = 0

for i in range(len(pulsesresult['results'])): 
	print("\n #########writing CSV file#########","count ",count,".\n")
	writer.writerow([str(pulsesresult['results'][i]['author_name']),str(pulsesresult['results'][i]['created']),str(pulsesresult['results'][i]['description']),str(pulsesresult['results'][i]['industries']),str(pulsesresult['results'][i]['malware_families']),str(pulsesresult['results'][i]['name']),str(pulsesresult['results'][i]['references']),str(pulsesresult['results'][i]['tags']),str(pulsesresult['results'][i]['targeted_countries'])])
	count = count + 1

from google.colab import files
files.download('/content/ransomtoday.csv')
