#coding=utf-8
import sys
import atexit
from PyQt4 import QtGui,QtCore
import MainWindow





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = MainWindow.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



