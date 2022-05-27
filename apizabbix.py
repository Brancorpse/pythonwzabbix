from pyzabbix import ZabbixAPI
import configparser

# Função para ser chamada por outros arquivos para logar no Zabbix e fazer as consultas
# Function to be called by other files, to log in Zabbix and do searchings
def connect():
    config = configparser.ConfigParser()
    config.read("config.ini")

    user = config.get('zabbix', 'user')
    password = config.get('zabbix', 'password')
    server = config.get('zabbix', 'server')
# Criando objeto de conexão para fazer o login na ferramenta
# Creating a connection object to make login in the tool

    zapi = ZabbixAPI(server)
    # zapi.session.verify = False
    zapi.login(user, password)
    return zapi
