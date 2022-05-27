import apizabbix

# Adiocionado filtro que exclui para remover os grupos de são de templates

api = apizabbix.connect()
hostgroups = api.hostgroup.get(
    output = 'extend',
    excludeSearch=True,
    search={'name': 'Templates'
            }
)

for hostgroup in hostgroups:
    print(hostgroup['name'])

api.user.logout()

