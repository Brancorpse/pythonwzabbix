import apizabbix

# Correlação de dados usando Python. Pegaremos dados de todos os eventos de um grupo para fazer o filtro
# English: Data correlation using Python. We'll catch data from all events of a group to make a filter

api = apizabbix.connect()
hostgroups = api.hostgroup.get(
    output=['id'],
    filter={
        'name': 'Portal'
    },
)
# Adicionado filtro
# English: Adding filter

events = api.event.get(
    output=[
        'clock',
        'name',
        'value',
        'severity',
    ],
    groupids=hostgroups[0]['groupid'],
)
# Lista de severidades
# English: severity list
severidades = [
    'Não classificada',
    'Informação',
    'Atenção',
    'Alta',
    'Desastre'
]

from datetime import datetime
for event in events:
    hora_evento = datetime.fromtimestamp(
        int(event['clock'])
    ) .strftime('%Y-%m-%d %H: %M:%S')
    severidade = severidades[(int(event['severity']))]
    print(
        'Evento: '+event['name']+ ',  ocorrido em: '+ hora_evento +' com severidade ' + severidade
    )

api.user.logout()
