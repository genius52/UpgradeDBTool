#coding=utf-8
from PyQt4.Qt import Qt, QObject,QLineEdit,QTextEdit
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from PyQt4 import QtGui, QtCore
import os


class DirLineEdit(QLineEdit, QtCore.QObject):
    @pyqtSlot(QtCore.QString)
    def mytextChanged(self, string):
        # QtGui.QMessageBox.information(self,"Hello!","Current String is:\n"+string)
        if not os.path.exists(string):
            self.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.setStyleSheet("color: rgb(0, 0, 0);")

    def __init__(self):
        super(DirLineEdit, self).__init__()
        self.connect(self, SIGNAL("textChanged(QString)"),
                     self, SLOT("mytextChanged(QString)"))
