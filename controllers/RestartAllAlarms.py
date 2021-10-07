import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)).replace('\\controllers', ''))

from controllers.Manager import AlarmManager
from subprocess import Popen, check_output

alarms = AlarmManager.getAll()
AlarmManager.clearData()

for a in alarms:
	Popen(['pythonw', '../controllers/WaitHour.pyw', a['title'], a['time']], shell=False)