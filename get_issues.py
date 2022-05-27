import requests
import json
from datetime import datetime



ZABBIX_API_URL = "http://zabbixm1.metroweb.sp.gov.br/zabbix/api_jsonrpc.php"
UNAME = "e009349"
PWORD = "Chem1c@l01"



r = requests.post(ZABBIX_API_URL,
json={
"jsonrpc": "2.0",
"method": "user.login",
"params": {
"user": UNAME,
"password": PWORD},
"id": 1
})



#print(json.dumps(r.json(), indent=4, sort_keys=True))



AUTHTOKEN = r.json()["result"]



# Retrieve a list of problems
#print("\nRetrieve a list of problems")
r = requests.post(ZABBIX_API_URL,
json={
"jsonrpc": "2.0",
"method": "event.get",
"params": {
"time_from": "1653550816",
"time_till": "1653551816",
"output": "extend",
"selectHosts": "extend",
"selectAcknowledges": "extend",
"recent": "true",
"sortfield": ["eventid"],
"sortorder": "DESC"
},
"id": 2,
"auth": AUTHTOKEN
})



#print(json.dumps(r.json(), indent=4, sort_keys=True))
j = r.json()["result"]
for nameinc in j:
    clockinc = int(nameinc['clock'])
for namehost in nameinc['hosts']:
    nameserver = namehost['host']
print(nameinc['name']," #Gerenciamento de Rede - ",datetime.utcfromtimestamp(clockinc).strftime('%d-%m-%Y')," - ",datetime.utcfromtimestamp(clockinc).strftime('%H:%M:%S')," - ", nameserver, " - ",nameinc['name'])
#print(datetime.utcfromtimestamp(clockinc).strftime('%Y-%m-%d %H:%M:%S'))
#print(j[0])