from typing import Counter
import shodan
import sys
# Configuration
API_KEY = "Enter your key here"
api = shodan.Shodan(API_KEY)
number = 0
##https://readthedocs.org/projects/shodan/downloads/pdf/latest/
##https://www.linkedin.com/pulse/how-search-icsscada-systems-using-shodan-muhammad-mesbah/
#print(api)
#Example search 
results = api.search('SCADA  port:502')
print('Results found: {}'.format(results['total']))
for result in results['matches']:
	number = number + 1
	print ('############ hit ',number,'##########')
	print('IP: {}'.format(result['ip_str']))
	print('##data##')
	print(result['data'])
	print('')
	print('##ISP##')
	print(result['isp'])
	print('')
	print('##location##')
	print(result['location'])
	print('')
	print('##org##')
	print(result['org'])
	print('')
	print('##port##')
	print(result['port'])
	

