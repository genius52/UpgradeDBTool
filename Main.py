#coding=utf-8
import os
import FileCompare
import re

# def TestRegex(s,filecontent):
#     pattern = r".*create table (\S+).*%s.*" % s.replace('(',"\(").replace(')',"\)")
#     regex = re.compile(pattern,re.DOTALL)
#     m = regex.match(filecontent)
#     if m:
#         print m.groups(1)
#         return m.groups(1)#     return None

if __name__ == '__main__':
    oldSql = "D:\diff1.txt"
    newSql = "D:\diff2.txt"
    upgradeSql = "D:\upgrade.sql"

    f = open("d:/difftest.txt",'r')
    s = r"uid                  varchar(64)"
    content = f.read()
    # TestRegex(s,content)

    sql = FileCompare.GenerateUpgradeSql(oldSql,newSql)
    if len(sql) > 0:
        f = open(upgradeSql,"wt")
        f.write(sql)
        f.close()
    print sql
    # command = bcExe,"/silent",diffFile,oldSql,newSql,resultFile
    # ret = os.system(command)
    # print ret

#Get lastest version DB sql
#Compare with the previous sql
#Generate DB upgrade sql
#Update system data convertor code

