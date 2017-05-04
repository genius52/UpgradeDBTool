# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpgradeTool.ui'
#
# Created: Thu May 04 17:15:38 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.textOldSql = QtGui.QTextEdit(Dialog)
        self.textOldSql.setGeometry(QtCore.QRect(100, 20, 241, 31))
        self.textOldSql.setObjectName(_fromUtf8("textOldSql"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textNewSql = QtGui.QTextEdit(Dialog)
        self.textNewSql.setGeometry(QtCore.QRect(100, 80, 241, 31))
        self.textNewSql.setObjectName(_fromUtf8("textNewSql"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textDbcode = QtGui.QTextEdit(Dialog)
        self.textDbcode.setGeometry(QtCore.QRect(100, 130, 241, 31))
        self.textDbcode.setObjectName(_fromUtf8("textDbcode"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 81, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(254, 180, 91, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "SQL脚本(旧)", None))
        self.label_2.setText(_translate("Dialog", "SQL脚本(新)", None))
        self.label_3.setText(_translate("Dialog", "DB代码", None))
        self.pushButton.setText(_translate("Dialog", "生成升级脚本", None))
        self.pushButton_2.setText(_translate("Dialog", "更新代码", None))
        self.pushButton_3.setText(_translate("Dialog", "更新DBWrapper", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

