import filecmp
import difflib
import sys

def CompareSqlFile(oldSql,newSql):
    # oldFile = open(oldSql,'r')
    # newFile = open(newSql,'r')
    if oldSql == "" or newSql=="":
        print "Usage: test.py filename1 filename2"
        sys.exit()
    text1_lines = readline(oldSql)
    text2_lines = readline(newSql)
    d = difflib.HtmlDiff()
    print d.make_file(text1_lines,text2_lines)

def readline(filename):
    fileHandle = open (filename,'rb')
    text = fileHandle.read().splitlines()
    fileHandle.close()
    return text

