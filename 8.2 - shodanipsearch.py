import shodan
import sys
# Configuration
API_KEY = "enter your key"
api = shodan.Shodan(API_KEY)
number = 0
host = api.host('8.8.8.8')
# Print general info
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
