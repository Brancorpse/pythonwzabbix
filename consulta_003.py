import apizabbix

'''Novo filtro. Dessa vez, adicionando 'Select Hosts' para fazer a correlação entre dados
 e filtro de campos.
 '''

api = apizabbix.connect()
hostgroups = api.hostgroup.get(
    output = 'extend',
    excludeSearch=True,
    search={'name': 'Templates'
            },
    selectHosts=['name','host']
)

'''Foi necessário um loop novo a cada novo grupo, já que veio uma lista de
vários dicionários e informações, sendo um para cada host
'''

for hostgroup in hostgroups:
    print('Grupo: ', hostgroup['name'])
    for host in hostgroup['hosts']:
        print('     Host: '+host['name']+': '+host['host'])

api.user.logout()

