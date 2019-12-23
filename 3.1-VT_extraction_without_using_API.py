
Here is an approach using the ajax calls :

import requests
import json

headers = {
    'pragma': 'no-cache',
    'x-app-hostname': 'https://www.virustotal.com/gui/',
    'dnt': '1',
    'x-app-version': '20190611t171116',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,mt;q=0.5',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'accept': 'application/json',
    'cache-control': 'no-cache',
    'authority': 'www.virustotal.com',
    'referer': 'https://www.virustotal.com/',
}

response = requests.get('https://www.virustotal.com/ui/files/f8ee4c00a3a53206d8d37abe5ed9f4bfc210a188cd5b819d3e1f77b34504061e', headers=headers)
data = json.loads(response.content)
malicious = data['data']['attributes']['last_analysis_stats']['malicious']
undetected = data['data']['attributes']['last_analysis_stats']['undetected']

print(malicious, 'malicious out of', malicious + undetected)
