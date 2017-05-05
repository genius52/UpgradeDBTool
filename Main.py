#coding=utf-8
import sys
from PyQt4 import QtGui,QtCore
import FileCompare
import MainWindow





if __name__ == '__main__':
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


