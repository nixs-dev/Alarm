# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alert.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.insert(0, os.getcwd().replace('\\views', ''))

from controllers.AudioPlayer import AudioPlayer
from subprocess import Popen


class Ui_AlertWindow(object):

    window = None
    thread = None

    def postpone(self):
        title = self.thread.title
        timeData = self.thread.hour.split(':')

        newTime = str(timeData[0]) + ':' + str(int(timeData[1]) + 1)

        Popen(["pythonw", os.getcwd() + "/controllers/WaitHour.pyw", title, newTime], shell=False)
        self.window.close()

    def finishAlarm(self):
        self.window.close()

    def startSong(self):
        soundPath = os.getcwd() + '/assets/notificationSound.mp3'
        player = AudioPlayer(soundPath)
        player.play(player)

    def setupData(self, thread):
        self.alarmTitle.setText(thread.title)
        self.alarmHour.setText(thread.hour)

    def myConfig(self, Alert):
        Alert.setWindowFlag(QtCore.Qt.FramelessWindowHint) 

    def setupUi(self, AlertWindow, thread):
        self.window = AlertWindow
        self.thread = thread

        AlertWindow.setObjectName("AlertWindow")
        AlertWindow.setWindowModality(QtCore.Qt.NonModal)
        AlertWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(AlertWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.alertIcon = QtWidgets.QLabel(self.centralwidget)
        self.alertIcon.setGeometry(QtCore.QRect(120, 10, 81, 61))
        self.alertIcon.setText("")
        self.alertIcon.setPixmap(QtGui.QPixmap(os.getcwd() + "/assets/alertIcon.png"))
        self.alertIcon.setScaledContents(True)
        self.alertIcon.setObjectName("alertIcon")
        self.alarmTitle = QtWidgets.QLabel(self.centralwidget)
        self.alarmTitle.setGeometry(QtCore.QRect(90, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.alarmTitle.setFont(font)
        self.alarmTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmTitle.setObjectName("alarmTitle")
        self.alarmHour = QtWidgets.QLabel(self.centralwidget)
        self.alarmHour.setGeometry(QtCore.QRect(90, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.alarmHour.setFont(font)
        self.alarmHour.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmHour.setObjectName("alarmHour")
        self.postponeAlarm = QtWidgets.QPushButton(self.centralwidget)
        self.postponeAlarm.setGeometry(QtCore.QRect(50, 170, 75, 41))
        self.postponeAlarm.setObjectName("postponeAlarm")
        self.stopAlarm = QtWidgets.QPushButton(self.centralwidget)
        self.stopAlarm.setGeometry(QtCore.QRect(170, 170, 75, 41))
        self.stopAlarm.setObjectName("stopAlarm")
        AlertWindow.setCentralWidget(self.centralwidget)


        self.stopAlarm.clicked.connect(self.finishAlarm)
        self.postponeAlarm.clicked.connect(self.postpone)
        self.myConfig(AlertWindow)
        self.startSong()
        self.retranslateUi(AlertWindow)
        QtCore.QMetaObject.connectSlotsByName(AlertWindow)

    def retranslateUi(self, AlertWindow):
        _translate = QtCore.QCoreApplication.translate
        AlertWindow.setWindowTitle(_translate("AlertWindow", "MainWindow"))
        self.alarmTitle.setText(_translate("AlertWindow", "TITLE"))
        self.alarmHour.setText(_translate("AlertWindow", "HOUR"))
        self.postponeAlarm.setText(_translate("AlertWindow", "Adiar"))
        self.stopAlarm.setText(_translate("AlertWindow", "Parar"))

        #self.setupData(thread)

