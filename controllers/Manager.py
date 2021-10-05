import os
import json

class AlarmManager():
	data_path = os.getcwd().replace('\\controllers', '') + '\\activeAlarms.tm'

	def saveAlarm(data_list):
		with open(AlarmManager.data_path, 'a+') as file_:
			content = {"ID": data_list['id'],
					  "title": data_list['title'],
					  "time": data_list['time']
					  }
			file_.write(str(content) + '\n')

	def getAll():
		alarms = []
		with open(AlarmManager.data_path, 'r') as file_:
			for line in file_.readlines():
				line = line.replace("'", '"')

				if line != '':
					alarm = json.loads(line)
					alarms.append(alarm)
		return alarms

	def checkIsEnabled(id_):
		alarms = AlarmManager.getAll()

		for a in alarms:
			if a['ID'] == id_:
				return True

		return False

	def removeAlarm(id_):
		alarms = AlarmManager.getAll()
		content_to_rewrite = ''

		for i, a in enumerate(alarms):
			if a['ID'] == id_:
				alarms.pop(i)

		for a in alarms:
			content_to_rewrite += str(a) + '\n'

		with open(AlarmManager.data_path, 'w') as file_:
			file_.write(content_to_rewrite)
