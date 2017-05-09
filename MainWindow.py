# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri May 05 17:25:04 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4.Qt import Qt, QObject,QLineEdit
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT,QString
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QColor,QMessageBox
import os
import sys
import difflib
import re
import FileCompare
import GlobalSetting
import DirEdit

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

        # self.textOldSql = QtGui.QLineEdit(self.groupBoxUpgrade)
        self.textOldSql = DirEdit.DirLineEdit()
        self.textOldSql.setParent(self.groupBoxUpgrade)
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
        self.textNewSql = DirEdit.DirLineEdit()
        self.textNewSql.setParent(self.groupBoxUpgrade)
        self.textNewSql.setGeometry(QtCore.QRect(100, 60, 641, 31))
        self.textNewSql.setObjectName(_fromUtf8("textNewSql"))
        self.textUpgradeSql = DirEdit.DirLineEdit()
        self.textUpgradeSql.setParent(self.groupBoxUpgrade)
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
        self.textDbwrapper = DirEdit.DirLineEdit()
        self.textDbwrapper.setParent(self.groupBoxDbwrapper)
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
        self.textConvertor = DirEdit.DirLineEdit()
        self.textConvertor.setParent(self.groupBoxSystemData)
        self.textConvertor.setGeometry(QtCore.QRect(100, 60, 641, 31))
        self.textConvertor.setObjectName(_fromUtf8("textConvertor"))
        self.labelDatamodel = QtGui.QLabel(self.groupBoxSystemData)
        self.labelDatamodel.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.labelDatamodel.setObjectName(_fromUtf8("labelDatamodel"))
        self.textDatamodel = DirEdit.DirLineEdit()
        self.textDatamodel.setParent(self.groupBoxSystemData)
        self.textDatamodel.setGeometry(QtCore.QRect(100, 20, 641, 31))
        self.textDatamodel.setObjectName(_fromUtf8("textDatamodel"))

        self.upgradeSqlButton.clicked.connect(self.upgradeSql)
        self.updateDBWrapperButton.clicked.connect(self.updateDbwrapper)
        self.updateSystemdataButton.clicked.connect(self.updateSystemdata)
        self.textNewSql.setText(GlobalSetting.New_Tmssql)
        self.textOldSql.setText(GlobalSetting.Old_Tmssql)
        self.textDbwrapper.setText(GlobalSetting.Dbwrapper_Design)
        self.textDatamodel.setText(GlobalSetting.Systemdata_Datamodel)
        self.textConvertor.setText(GlobalSetting.Systemdata_Convertor)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def upgradeSql(self):
        try:
            oldSqlPath = str(self.textOldSql.text())
            newSqlPath = str(self.textNewSql.text())
            # oldSqlPath = "D:\diff1.txt"
            # newSqlPath = "D:\diff2.txt"
            sql = FileCompare.GenerateUpgradeSql(oldSqlPath,newSqlPath)
            if sql != None:
                self.textUpgradeSql.setText(os.path.join(os.getcwd(),"upgrade.sql"))
                with open(str(self.textUpgradeSql.text),"wt") as newsql:
                    newsql.write(sql)
        except Exception as e:
            QMessageBox.information(None, "upgradeSql FAIL!", QString(e.message()))


    def updateDbwrapper(self):
        #执行新的Sql->更新dbwrapper->修改Design.cs文件
        crcTool = os.path.join(os.getcwd(),GlobalSetting.CrcDbwrapper_TOOL)
        cmd = "%s %s"%(crcTool,str(self.textDbwrapper.text()))
        result = os.system(cmd)
        if result != 0:
            QMessageBox.information(None,"",u"更新DBWrapper失败")

    def GenerateVarDefinition(self,attrtype, attr):
        definiton = "\t\t[DataMember]\n\t\tpublic"
        if "char" in attrtype:
            definiton = definiton + " string " + attr.capitalize() + ";\n"
        elif "float" in attrtype:
            definiton = definiton + " float " + attr.capitalize() + ";\n"
        elif "int" in attrtype:
            definiton = definiton + " int " + attr.capitalize() + ";\n"
        return definiton

    def AddAttributeInFile(self,table, attrtype, attr):
        pattern = "public class DM_%s" % table.capitalize()
        classDefPos = 0
        lines = []
        datamodelfile = open(str(self.textDatamodel.text()),'r')
        for line in datamodelfile:  # 内置的迭代器, 效率很高
            lines.append(line)
        datamodelfile.close()
        for line in lines:
            if pattern in line:
                defVal = self.GenerateVarDefinition(attrtype,attr)
                lines.insert(classDefPos + 2,defVal)
                break
            classDefPos += 1
        datamodelfile = open(str(self.textDatamodel.text()),'w')
        datamodelfile.writelines(lines)
        datamodelfile.close()

    def GenerateConvertorExpression(self, attrtype, attr):
        toDatamodelExpression = "\t\t\tdmObject.%s = efObject.%s;\n" % (attr.capitalize(),attr)
        toEFObjectExpression = "\t\t\tefObject.%s = dmObject.%s;\n" % (attr,attr.capitalize())
        return toDatamodelExpression,toEFObjectExpression

    def AddConvertorInFile(self,table, attrtype, attr):
        toDatamodelPattern = "public static DM_%s ToDataModel" % table.capitalize()
        toEFPattern = "public static %s ToEFObject" % table
        classDefPos = 0
        lines = []
        convertorfile = open(str(self.textConvertor.text()),'r')
        for line in convertorfile:
            lines.append(line)
        convertorfile.close()
        (toDatamodel, toEFObject) = self.GenerateConvertorExpression(attrtype, attr)
        insertLineTag = 0
        for line in lines:
            if toDatamodelPattern in line:
                lines.insert(classDefPos + 5,toDatamodel)
                insertLineTag += 1
            if toEFPattern in line:
                lines.insert(classDefPos + 5, toEFObject)
                insertLineTag += 1
            if insertLineTag >= 2:
                break
            classDefPos += 1
        convertorfile = open(str(self.textConvertor.text()),'w')
        convertorfile.writelines(lines)
        convertorfile.close()

    def ModifySystemdataCode(self,oldSql, newSql):
        try:
            oldfile = open(oldSql, 'r')
            oldlcontent = oldfile.read()
            newfile = open(newSql, 'r')
            newcontent = newfile.read()
            diff = difflib.ndiff(oldlcontent.splitlines(), newcontent.splitlines())
            for diffline in diff:
                if diffline.startswith('+'):
                    tablename = FileCompare.FindRelatedTable(diffline[1:].strip(), newcontent)
                    if tablename != None:
                        valueType = diffline[1:].strip().split()
                        if len(valueType) > 2:
                            self.AddAttributeInFile(tablename, valueType[1], valueType[0])
                            self.AddConvertorInFile(tablename, valueType[1], valueType[0])
                elif diffline.startswith('-'):
                    print "Delete %s" % diffline[1:]

        except Exception as e:
            QMessageBox.information(None, "ModifySystemdataCode FAIL!", QString(e.message()))

    def updateSystemdata(self):
        try:
            # oldSqlPath = "D:\diff1.txt"
            # newSqlPath = "D:\diff2.txt"
            oldSqlPath = str(self.textOldSql.text())
            newSqlPath = str(self.textNewSql.text())
            result = self.ModifySystemdataCode(oldSqlPath,newSqlPath)
            if result:
                print result
        except Exception as e:
            QMessageBox.information(None,"updateSystemdata FAIL!",QString(e.message()))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "数据库升级工具", None))
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

