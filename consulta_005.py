import apizabbix

# Correlação de dados usando Python. Pegaremos dados de todos os eventos de um grupo para fazer o filtro
# English: Data correlation using Python. We'll catch data from all events of a group to make a filter

api = apizabbix.connect()

# Adicionado filtro
# English: Adding filter

historico = api.history.get({
    'itemids': [23668],
    'history':0,
    'output': 'extend',
    'time_from': 1438387200,
    'time_till': 1439250959
})
print(historico)


api.user.logout()
