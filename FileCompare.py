import filecmp
import difflib
import sys
import re

def FindRelatedTable(s,filecontent):
    pattern = r".*create table (\S+).*%s.*\)" % s.replace('(',"\(").replace(')',"\)")
    regex = re.compile(pattern,re.DOTALL)
    m = regex.match(filecontent)
    if m:
        print m.group(1)
        return m.group(1)
    return None

def GenerateDeleteAttributeSql(table,attr):
    pattern = r"(\S+)\s+(\S+)\s\S.*"
    m = re.match(pattern,attr.strip())
    if m:
        print "Delete" ,m.group(1)
        sql = "alter table %s drop column %s;" % (table,m.group(1))
        return sql
    return None

def GenerateAddAttributeSql(table,attr):
    pattern = r"(\S+)\s+(\S+)\s\S.*"
    m = re.match(pattern,attr.strip())
    if m:
        print "Add" ,m.group(1)
        sql = "alter table %s add column %s %s;" % (table,m.group(1),m.group(2))
        return sql
    return None

def GenerateModifyAttributeSql(s):
    print "Modify",s.strip()
    return

def GenerateDeleteTableSql(s):
    print "Delete table",s.strip()
    return

def GenerateAddTableSql(s):
    print "Add table",s.strip()
    return

def GenerateUpgradeSql(oldSql,newSql):
    try:
        oldFile = open(oldSql,'r')
        newFile = open(newSql,'r')
        if oldSql == "" or newSql == "":
            print "Usage: test.py filename1 filename2"
            sys.exit()
        text1_lines = oldFile.read().splitlines()
        text2_lines = newFile.read().splitlines()
        oldlines = open(oldSql, 'r').read()
        newlines = open(newSql, 'r').read()
        diff = difflib.ndiff(text1_lines,text2_lines)
        upgradeSql = 'use rt_tms;\n'
        for d in list(diff):
            if d.find('-') == 0:#'delete attribute in old sql'
                tablename = FindRelatedTable(d[1:].strip(),oldlines)
                if tablename != None:
                    sentence = GenerateDeleteAttributeSql(tablename,d[1:])
                    if sentence != None:
                        upgradeSql = upgradeSql + sentence + '\n'
            elif d.find('+') == 0:
                tablename = FindRelatedTable(d[1:].strip(), newlines)
                if tablename != None:
                    sentence = GenerateAddAttributeSql(tablename,d[1:])
                    if sentence != None:
                        upgradeSql = upgradeSql + sentence + '\n'
            elif d.find('?') == 0:
                print "unclear modify exist ",d
        return upgradeSql
    except:
        oldFile.close()
        newFile.close()
        return None

