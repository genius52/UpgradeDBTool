#coding=utf-8
import os
import FileCompare

if __name__ == '__main__':
    print "Start upgrade DB"
    oldSql = "D:/RT_TMS/MAIN/Scripts/TSS/AppServer/InstallScripts/TMSDB.sql"
    newSql = "D:/RT_TMS/Doc/DataModel/TMSDB.sql"
    bcExe = "\"C:/Program Files (x86)/Beyond Compare 3/BCompare.exe\""
    diffFile = "\"@D:/diff.txt\""
    resultFile = "\"D:/BCompare.HTML\""

    FileCompare.CompareSqlFile(oldSql,newSql)
    # command = bcExe,"/silent",diffFile,oldSql,newSql,resultFile
    # ret = os.system(command)
    # print ret

#Get lastest version DB sql
#Compare with the previous sql
#Generate DB upgrade sql
#Update system data convertor code
