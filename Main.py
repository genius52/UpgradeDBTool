#coding=utf-8
import sys
import atexit
from PyQt4 import QtGui,QtCore
import MainWindow





if __name__ == '__main__':
    # with open("D:\RT_TMS\MAIN\Scripts\TSS\AppServer\InstallScripts\TMSDB.sql", 'r+') as newfile:
    #     newlines = newfile.readlines()

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = MainWindow.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    # oldSql = "D:\diff1.txt"
    # newSql = "D:\diff2.txt"
    # upgradeSql = "D:\upgrade.sql"
    #
    # sql = FileCompare.GenerateUpgradeSql(oldSql,newSql)
    # if len(sql) > 0:
    #     f = open(upgradeSql,"wt")
    #     f.write(sql)
    #     f.close()
    # print sql


