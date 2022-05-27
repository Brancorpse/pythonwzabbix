import apizabbix

# Adiocionado consulta de host no Zabbix via Python

# English: Add host search in Zabbix using Python

api = apizabbix.connect()
hostgroups = api.hostgroup.get()

# Mostrando os resultados

# English: Showing results

from pprint import pprint
pprint(hostgroups)

api.user.logout()