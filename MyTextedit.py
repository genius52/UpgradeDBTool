#coding=utf-8
from PyQt4.Qt import Qt, QObject,QLineEdit,QTextEdit
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from PyQt4 import QtGui, QtCore
import os
import sys
import GlobalSetting

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


app = QtGui.QApplication(sys.argv)
smObj = DirLineEdit()

smObj.show()

app.exec_()

#
# class MyButton(QtGui.QPushButton):
#     myclicked = QtCore.pyqtSignal(int)
#     def __init__(self, _id, *args, **kwargs):
#         QtGui.QPushButton.__init__(self, *args, **kwargs)
#         self._id = _id
#         self.connect(self, QtCore.SIGNAL("clicked()"), self.emitMyclicked)
#     def emitMyclicked(self):
#         self.myclicked.emit(self._id)
#
#
# app = QtGui.QApplication([])
# w = QtGui.QWidget()
# w.resize(300, 300)
#
# def showMsg(_id):
#     QtGui.QMessageBox.information(w, u"信息", u"查看 %d" % _id)
#
# def showText(s):
#     QtGui.QMessageBox.information(w, u"信息", u"查看 %d" % s)
#
# btn = MyButton(1, u"查看1", w)
# w.connect(btn, QtCore.SIGNAL("myclicked(int)"), showMsg)
#
# txt = MyTextedit()
# txt.move(100,100)
# w.connect(txt,QtCore.SIGNAL("mytextchanged(QString)"),showText)
#
# # btn2 = MyButton(2, u"查看2", w)
# # btn2.move(0, 30)
# # w.connect(btn2, QtCore.SIGNAL("myclicked(int)"), showMsg)
#
# w.show()
# app.exec_()