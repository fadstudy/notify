from os import environ
from datetime import datetime, timedelta
from notify import Notify
import config
import run

with open('.env') as file_:
    for line in file_:
        variable = [x.strip() for x in line.split('=')]
        environ['{0}'.format(variable[0])] = '{0}'.format(variable[1])

config.HOUR = datetime.utcnow() + timedelta(hours=11)     
port = int(environ.get('PORT', 5000))        
run()
debug=True

