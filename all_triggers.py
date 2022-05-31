import sys

import apizabbix

# Connecting Zabbix library

api = apizabbix.connect()

# getting triggers

triggers = api.trigger.get()
len(triggers)
482
sys.getsizeof(triggers)
4280
# showing triggers

print(triggers)