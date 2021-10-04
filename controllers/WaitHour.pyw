import sys
import os

sys.path.insert(0, os.getcwd().replace('\\controllers', ''))

from threading import Thread
from datetime import datetime
from playsound import playsound
from views import Alert
from PyQt5 import QtCore, QtGui, QtWidgets

class WaitHour(Thread):

    def __init__(self, title, hour):
        super().__init__()
        self.title = title
        self.hour = hour + ':00'

    def run(self):
        while datetime.now().strftime("%H:%M:%S") != self.hour:
            pass

        app = QtWidgets.QApplication(sys.argv)
        AlertWindow = QtWidgets.QMainWindow()
        ui = Alert.Ui_AlertWindow()
        ui.setupUi(AlertWindow, self)
        AlertWindow.show()
        sys.exit(app.exec_())
        
args = sys.argv

thr = WaitHour(args[1], args[2])

thr.start()