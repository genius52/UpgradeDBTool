import filecmp
import difflib
import sys
import re

def FindRelatedTable(s,filecontent):
    pattern = r".*create table (\S+).*%s.*\)" % s.replace('(',"\(").replace(')',"\)")
    regex = re.compile(pattern,re.DOTALL)
    m = regex.match(filecontent)
    if m:
        return m.group(1)
    return None

def GenerateDeleteAttributeSql(table,attr):
    pattern = r"(\S+)[\s\t]+(\S+)[\s\n]*"
    m = re.match(pattern,attr.strip())
    if m:
        print "Delete" ,m.group(1)
        sql = "alter table %s drop column %s;" % (table,m.group(1))
        return sql
    return None

def GenerateAddAttributeSql(table,attr):
    pattern = r"(\S+)[\s\t]+(\S+)[\s\n]*"
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
    pattern = r"create table\s*(\S+)[\s\n]*"
    m = re.match(pattern,s.strip())
    if m:
        sql = "drop table %s;" % m.group(1)
        return sql
    return None

def GenerateCreateTableSql(createtableline,filecontent):
    print "Add table",createtableline.strip()
    pattern = r"%s.*)\n\n" % createtableline
    m = re.match(pattern,createtableline.strip())
    if m:
        sql = "create table %s;" % m.group(1)
        return sql
    return None

def GenerateUpgradeSql(oldSql,newSql):
    try:
        oldfile = open(oldSql, 'r')
        oldlcontent = oldfile.read()
        newfile = open(newSql, 'r')
        newcontent = newfile.read()
        diff = difflib.ndiff(oldlcontent.splitlines(),newcontent.splitlines())
        sqlPrefix = "use rt_tms;\n"
        upgradeSql = sqlPrefix
        print list(diff)
        for d in diff:
            if d.startswith('-') == 0:#'delete attribute in old sql'
                if d.startswith("create table"):
                    delTableSql = GenerateDeleteTableSql(d[1:])
                    if delTableSql != None:
                        upgradeSql = upgradeSql + delTableSql + '\n'
                        continue
                tablename = FindRelatedTable(d[1:].strip(), oldlcontent)
                if tablename != None:
                    delAttrSql = GenerateDeleteAttributeSql(tablename,d[1:])
                    if delAttrSql != None:
                        upgradeSql = upgradeSql + delAttrSql + '\n'
            elif d.startswith('+') == 0:
                # if d.find("create table"):
                #     createTableSql = GenerateCreateTableSql(d[1:],newlines)
                #     if createTableSql != None:
                #         upgradeSql = upgradeSql + createTableSql + '\n'
                tablename = FindRelatedTable(d[1:].strip(), newcontent)
                if tablename != None:
                    sentence = GenerateAddAttributeSql(tablename,d[1:])
                    if sentence != None:
                        upgradeSql = upgradeSql + sentence + '\n'
            elif d.startswith('?') == 0:
                print "unclear modify exist ",d
        if cmp(upgradeSql,sqlPrefix) == 0:
            return "equal"
        else:
            return upgradeSql
    except Exception as e:
        print e
        return None
