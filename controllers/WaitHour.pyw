import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)).replace('\\controllers', ''))

from threading import Thread
from datetime import datetime
from playsound import playsound
from random import randint
from views import Alert
from controllers.Manager import AlarmManager
from PyQt5 import QtCore, QtGui, QtWidgets

class WaitHour(Thread):

    def __init__(self, title, hour):
        super().__init__()
        self.id = self.generateID()
        self.title = title
        self.hour = self.formatTime(hour)

        to_save = {'id': self.id,
                   'title': self.title,
                   'time': self.hour 
                  }

        AlarmManager.saveAlarm(to_save)


    def formatTime(self, time_):
        time_ = time_.split(':')
        for i, t in enumerate(time_):
            if len(t) == 1:
                time_[i] = '0' + str(t)

        return ':'.join(time_)
        
    def alertUser(self):
        app = QtWidgets.QApplication(sys.argv)
        AlertWindow = QtWidgets.QMainWindow()
        ui = Alert.Ui_AlertWindow()
        ui.setupUi(AlertWindow, self)
        AlertWindow.show()
        sys.exit(app.exec_())

    def generateID(self):
        return randint(0, 9999)

    def run(self):
        stoppedByUser = False

        while datetime.now().strftime("%H:%M:%S") != self.hour:
            if not AlarmManager.checkIsEnabled(self.id):
                stoppedByUser = True
                break

        if not stoppedByUser:
            self.alertUser()

    def eraseAlarmData(self):
        AlarmManager.removeAlarm(self.id)
        
args = sys.argv

thr = WaitHour(args[1], args[2])
thr.start()