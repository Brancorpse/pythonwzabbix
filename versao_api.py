from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://10.21.153.171/")
zapi.login("Admin","zabbix")
print("Conectado ao Zabbix API Versão %", zapi.api_version())

for h in zapi.host.get(output="extend"):
    print(h['hostid'])
