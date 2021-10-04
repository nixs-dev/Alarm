import sys
from views import Alert
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
AlertWindow = QtWidgets.QMainWindow()
ui = Alert.Ui_AlertWindow()
ui.setupUi(AlertWindow, None)
AlertWindow.show()
sys.exit(app.exec_())
