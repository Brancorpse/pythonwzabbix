import apizabbix

# Adiocionado consulta de host no Zabbix via Python

api = apizabbix.connect()
hostgroups = api.hostgroup.get()

from pprint import pprint
pprint(hostgroups)

api.user.logout()