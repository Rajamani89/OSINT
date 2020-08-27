import csv
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
import json
import time

#mykey
otx = OTXv2("YOUR KEY")


#otx searching
print("start querying")
pulsesresult = otx.search_pulses("tag:ransomware", max_results=2000)

#manupulating results
print("manupulating results")
size_output = len(pulsesresult['results'])
print(size_output,"results found based on the query")




# Writing to sample.json 
#print("writing in json file")
for i in range(0,size_output):
  print(i)
  with open("totalqueryresults2.json", "a") as outfile:
    print ("writing the number ",i,"pulse result")
    temppulseresult = pulsesresult['results'][i]
    json_object = json.dumps(temppulseresult, indent = 4)
    outfile.write(json_object)
    time.sleep(2)
    if i != size_output - 1:
        print("not the lastline")
        outfile.write(",\n")
    time.sleep(2)
    else:
      print("lastline")
        

