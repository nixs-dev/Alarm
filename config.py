import os


persistence_file = 'RerunAlarm.bat'
alarms_starter_file = 'RestartAllAlarms.py'
alarms_starter_path = os.getcwd() + '\\controllers\\' + alarms_starter_file
startup_path = os.getenv('APPDATA') + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + persistence_file
persistence_comamand = '''

@echo off

python "{0}"

'''.format(alarms_starter_path)


#Escreve/Reescreve o arquivo de reativação dos alarmes
with open(startup_path, 'w') as file_:
	file_.write(persistence_comamand)
