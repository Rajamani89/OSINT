import shodan
import sys
import time
API_KEY = "enter your api here"
api = shodan.Shodan(API_KEY)
number = 0
iplist = ['1.1.1.1',
'1.1.1.2',
'1.1.2.3',]
for i in iplist:
  print(i)
  number = number + 1
  print('############')
  print("sleeping for",i)
  time.sleep(5)
  print('############')
  print(number)
  print ('###Querying###')
  try:
    host = api.host(i)
  except Exception:
    pass
  print("""
  IP: {}
  Organization: {}
  Operating System: {}
  """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
# Print all banners
  for item in host['data']:
    print("""
    Port: {}
    Banner: {}
    """.format(item['port'], item['data']))
