import apizabbix

# Adiocionado filtro q para remover os grupos de são de templates
# English: Add filter to remove groups that aren't templates

api = apizabbix.connect()
hostgroups = api.hostgroup.get(
    output = 'extend',
    excludeSearch=True,
    search={'name': 'Templates'
            }
)
# Loop para imprimir apenas os nomes de grupos
# English: Loop just to print groups names

for hostgroup in hostgroups:
    print(hostgroup['name'])

api.user.logout()

