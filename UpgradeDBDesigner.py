#coding=utf-8
import os
import GlobalSetting



def UpgradeDBDesignerFile(dbDesignerFile):
    if os.path.exists(dbDesignerFile) == False:
        print dbDesignerFile
        return False;
    try:
        usingSerializationString = "using System.Runtime.Serialization;"
        usingCommonAlgorithmString = "using UIH.RT.CommonAlgorithm;"
        declareClassString = "public partial class tms"
        updatetimeString = "return _updatetime;"
        insteadUpdatetimeString = "                if (_updatetime.Year == 0001)return DateTime.Now;"
        GetRelatedCollectionString = "return ((IEntityWithRelationships)this).RelationshipManager.GetRelatedCollection<"
        returnEntitycollectionString = \
'''                try
                {
                    DBCRC.CheckFKReference(entityCollection);
                } 
                catch(CRCException ex)
                {
                    var dbWrapper = new RTDBWrapper();
                    dbWrapper.DealCRCResult(ex.Message);
                    return null;
                }
                return entityCollection;
'''
        GetRelatedReferenceString = "return ((IEntityWithRelationships)this).RelationshipManager.GetRelatedReference<"
        returnEntityString = \
'''                try
                {
                    DBCRC.CheckFKReference(entity);
                } 
                catch(CRCException ex)
                {
                    var dbWrapper = new RTDBWrapper();
                    dbWrapper.DealCRCResult(ex.Message);
                    return null;
                }
                return entity;
'''
        with open(dbDesignerFile, "r") as fRead:
            lines = fRead.readlines()
            with open(dbDesignerFile, "w") as fWrite:
                for line in lines:
                    if usingSerializationString in line:
                        fWrite.write(line)
                        fWrite.write(usingCommonAlgorithmString+"\n")
                    elif updatetimeString in line:
                        if insteadUpdatetimeString not in line:
                            fWrite.write(insteadUpdatetimeString + "\n")
                            fWrite.write(line)
                    elif GetRelatedCollectionString in line:
                        for table in GlobalSetting.ProtectedTables:
                            if table in line:
                                line = line.replace("return", "var entityCollection =")
                                fWrite.write(line)
                                fWrite.write(returnEntitycollectionString)
                                break
                        else:
                            fWrite.write(line)
                    elif GetRelatedReferenceString in line and "Value" in line:
                        for table in GlobalSetting.ProtectedTables:
                            if table in line:
                                line = line.replace("return", "var entity =")
                                fWrite.write(line)
                                fWrite.write(returnEntityString)
                                break
                        else:
                            fWrite.write(line)
                    elif declareClassString in line:
                        for table in GlobalSetting.ProtectedTables:
                            if table.strip('<').strip('>') + " " in line:
                                line = line.replace("EntityObject", "CRCObject")
                                print "CRCObject line: %s" % line
                        else:
                            fWrite.write(line)
                    else:
                        fWrite.write(line)
    except Exception as e:
        print e
        return False
    else:
        return True

if __name__ == "__main__":
    print "start update DB designer code"
    #UpgradeDBDesignerFile(GlobalSetting.Dbwrapper_Design)