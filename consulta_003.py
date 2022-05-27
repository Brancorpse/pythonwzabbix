import apizabbix

'''Novo filtro. Dessa vez, adicionando 'Select Hosts' para fazer a correlação entre dados
 e filtro de campos.
 
English: New filter. This time, adding 'Select Hosts' to make correlation between data and field filter 
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

English: That's was necessary a new loop for each new group, cuz it brought list of many dicionaries and 
informations, one for each host
'''

for hostgroup in hostgroups:
    print('Grupo: ', hostgroup['name'])
    for host in hostgroup['hosts']:
        print('     Host: '+host['name']+': '+host['host'])

api.user.logout()

