# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri May 05 17:25:04 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4.Qt import Qt, QObject,QLineEdit
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QColor
import os
import GlobalSetting

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
        Dialog.resize(891, 368)
        self.groupBoxUpgrade = QtGui.QGroupBox(Dialog)
        self.groupBoxUpgrade.setGeometry(QtCore.QRect(10, 10, 851, 141))
        self.groupBoxUpgrade.setAutoFillBackground(False)
        self.groupBoxUpgrade.setFlat(False)
        self.groupBoxUpgrade.setCheckable(False)
        self.groupBoxUpgrade.setObjectName(_fromUtf8("groupBoxUpgrade"))

        self.textOldSql = QtGui.QLineEdit(self.groupBoxUpgrade)
        self.textOldSql.setGeometry(QtCore.QRect(100, 20, 641, 31))
        self.textOldSql.setObjectName(_fromUtf8("textOldSql"))
        self.labelOldSql = QtGui.QLabel(self.groupBoxUpgrade)
        self.labelOldSql.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.labelOldSql.setObjectName(_fromUtf8("labelOldSql"))
        self.upgradeSqlButton = QtGui.QPushButton(self.groupBoxUpgrade)
        self.upgradeSqlButton.setGeometry(QtCore.QRect(760, 100, 81, 23))
        self.upgradeSqlButton.setObjectName(_fromUtf8("upgradeSqlButton"))
        self.labelNewSql = QtGui.QLabel(self.groupBoxUpgrade)
        self.labelNewSql.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.labelNewSql.setObjectName(_fromUtf8("labelNewSql"))
        self.textNewSql = QtGui.QTextEdit(self.groupBoxUpgrade)
        self.textNewSql.setGeometry(QtCore.QRect(100, 60, 641, 31))
        self.textNewSql.setObjectName(_fromUtf8("textNewSql"))
        self.textUpgradeSql = QtGui.QTextEdit(self.groupBoxUpgrade)
        self.textUpgradeSql.setGeometry(QtCore.QRect(100, 100, 641, 31))
        self.textUpgradeSql.setObjectName(_fromUtf8("textUpgradeSql"))
        self.labelUpgradeSql = QtGui.QLabel(self.groupBoxUpgrade)
        self.labelUpgradeSql.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.labelUpgradeSql.setObjectName(_fromUtf8("labelUpgradeSql"))
        self.groupBoxDbwrapper = QtGui.QGroupBox(Dialog)
        self.groupBoxDbwrapper.setGeometry(QtCore.QRect(10, 160, 851, 61))
        self.groupBoxDbwrapper.setObjectName(_fromUtf8("groupBoxDbwrapper"))
        self.updateDBWrapperButton = QtGui.QPushButton(self.groupBoxDbwrapper)
        self.updateDBWrapperButton.setGeometry(QtCore.QRect(750, 20, 91, 23))
        self.updateDBWrapperButton.setObjectName(_fromUtf8("updateDBWrapperButton"))
        self.textDbwrapper = QtGui.QTextEdit(self.groupBoxDbwrapper)
        self.textDbwrapper.setGeometry(QtCore.QRect(100, 20, 641, 31))
        self.textDbwrapper.setObjectName(_fromUtf8("textDbwrapper"))
        self.labelDbwrapper = QtGui.QLabel(self.groupBoxDbwrapper)
        self.labelDbwrapper.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.labelDbwrapper.setObjectName(_fromUtf8("labelDbwrapper"))
        self.groupBoxSystemData = QtGui.QGroupBox(Dialog)
        self.groupBoxSystemData.setGeometry(QtCore.QRect(10, 230, 851, 111))
        self.groupBoxSystemData.setObjectName(_fromUtf8("groupBoxSystemData"))
        self.updateSystemdataButton = QtGui.QPushButton(self.groupBoxSystemData)
        self.updateSystemdataButton.setGeometry(QtCore.QRect(750, 40, 91, 23))
        self.updateSystemdataButton.setObjectName(_fromUtf8("updateSystemdataButton"))
        self.labelConvertor = QtGui.QLabel(self.groupBoxSystemData)
        self.labelConvertor.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.labelConvertor.setObjectName(_fromUtf8("labelConvertor"))
        self.textConvertor = QtGui.QTextEdit(self.groupBoxSystemData)
        self.textConvertor.setGeometry(QtCore.QRect(100, 60, 641, 31))
        self.textConvertor.setObjectName(_fromUtf8("textConvertor"))
        self.labelDatamodel = QtGui.QLabel(self.groupBoxSystemData)
        self.labelDatamodel.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.labelDatamodel.setObjectName(_fromUtf8("labelDatamodel"))
        self.textDatamodel = QtGui.QTextEdit(self.groupBoxSystemData)
        self.textDatamodel.setGeometry(QtCore.QRect(100, 20, 641, 31))
        self.textDatamodel.setObjectName(_fromUtf8("textDatamodel"))

        # self.textOldSql.connect(self.textOldSql,SIGNAL("textChanged(QString)"),self,SLOT("textChanged(QString)"))
        # mytextchanged = QtCore.pyqtSignal(str)
        # self.textOldSql.emit(QtCore.SIGNAL("mytextchanged(str)"), self.textOldSql)
        # QtCore.QObject.connect(self.textOldSql, QtCore.SIGNAL(_fromUtf8("mytextchanged(str)")), self.oldSqlChanged)
        self.textOldSql.textChanged.connect(self.textChanged)

        self.upgradeSqlButton.clicked.connect(self.upgradeSql)
        self.updateDBWrapperButton.clicked.connect(self.updateDbwrapper)
        self.updateSystemdataButton.clicked.connect(self.updateSystemdata)
        if not os.path.exists(GlobalSetting.New_Tmssql):
            self.textNewSql.setTextColor(QColor(255,0,0))
        self.textNewSql.setText(GlobalSetting.New_Tmssql)
        # if not os.path.exists(GlobalSetting.Old_Tmssql):
            # self.textOldSql.setTextColor(QColor(255, 0, 0))
        self.textOldSql.setText(GlobalSetting.Old_Tmssql)
        if not os.path.exists(GlobalSetting.Dbwrapper_Design):
            self.textDbwrapper.setTextColor(QColor(255, 0, 0))
        self.textDbwrapper.setText(GlobalSetting.Dbwrapper_Design)
        if not os.path.exists(GlobalSetting.Systemdata_Datamodel):
            self.textDatamodel.setTextColor(QColor(255, 0, 0))
        self.textDatamodel.setText(GlobalSetting.Systemdata_Datamodel)
        if not os.path.exists(GlobalSetting.Systemdata_Convertor):
            self.textConvertor.setTextColor(QColor(255, 0, 0))
        self.textConvertor.setText(GlobalSetting.Systemdata_Convertor)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def textChanged(self,string):
        QtGui.QMessageBox.information("Hello!", "Current String is:\n" + string)
        return

    def upgradeSql(self):
        print self.textNewSql.toPlainText(),"upgradesql"
        return

    def updateDbwrapper(self):
        self.textDbwrapper.toPlainText()
        print "updateDbwrapper"
        return

    def updateSystemdata(self):
        self.textConvertor.toPlainText()
        print "updateConvertor"
        return

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBoxUpgrade.setTitle(_translate("Dialog", "升级脚本", None))
        self.labelOldSql.setText(_translate("Dialog", "SQL脚本(旧)", None))
        self.upgradeSqlButton.setText(_translate("Dialog", "生成升级脚本", None))
        self.labelNewSql.setText(_translate("Dialog", "SQL脚本(新)", None))
        self.labelUpgradeSql.setText(_translate("Dialog", "SQL升级脚本", None))
        self.groupBoxDbwrapper.setTitle(_translate("Dialog", "更新EF代码", None))
        self.updateDBWrapperButton.setText(_translate("Dialog", "更新DBWrapper", None))
        self.labelDbwrapper.setText(_translate("Dialog", "DB代码", None))
        self.groupBoxSystemData.setTitle(_translate("Dialog", "更新Systemdata代码", None))
        self.updateSystemdataButton.setText(_translate("Dialog", "更新Systemdata", None))
        self.labelConvertor.setText(_translate("Dialog", "Convertor", None))
        self.labelDatamodel.setText(_translate("Dialog", "Datamodel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

