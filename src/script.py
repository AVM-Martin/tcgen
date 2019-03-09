import sys;
import os;
import shutil as S;
import zipfile as Z;

root = os.getcwd(); #sys.argv[1];
zipPath = os.path.join(root, "problems.zip");
pdfPath = os.path.join(root, "problem.pdf");
iniPath = os.path.join(root, "domjudge-problem.ini");
yamlPath= os.path.join(root, "problem.yaml");
pdfPathDummy = os.path.join(os.path.dirname(os.path.realpath(__file__)), "problem.pdf");

def deleteIt(path):
    if(os.path.exists(path)): os.remove(path);

def isSampleTc(filename): return (len(filename.split('.')[0]) >= 9);

def getTcRelPath(filename):
    path = "data/secret";
    if(len(filename.split('.')[0]) == 4):
        filename = filename[:3] + "0" + filename[3:];
    if(len(filename.split('.')[0]) >= 9): path = "data/sample";
    # change out become ans extension
    if(len(filename.split('.')[1]) == 3):
        filename = filename[:-3] + "ans";
    # return
    return os.path.join(path, filename);

def createZip():
    zipf = Z.ZipFile(zipPath, "w", Z.ZIP_DEFLATED);
    # push all sample and secret tc
    lis = os.walk( os.path.join(root, "tc/tc") );
    for roots, dirs, files in lis:
        for file in files:
            filepath = os.path.join(roots, file);
            if(isSampleTc(file)): continue; # toggle
            zipf.write(filepath, getTcRelPath(file));
    # push problem statement
    zipf.write(pdfPath, "problem_statement/problem.pdf");
    zipf.write(pdfPath, "problem.pdf");
    # push domjudge-problem.ini
    zipf.write(iniPath, "domjudge-problem.ini");
    # push problem.yaml
    zipf.write(yamlPath, "problem.yaml");
    # close
    zipf.close();

def createIniFile(timeLimit):
    f = open(iniPath, "w");
    # print
    f.write("probid=\'\'\n");
    f.write("timelimit=\'{0}\'\n".format(timeLimit));
    # close
    f.close();

def createYamlFile(probName, memLimit, validFlag):
    f = open(yamlPath, "w");
    # print
    f.write("---\n");
    f.write("name: {0}\n".format(probName));
    f.write("validator_flags: {0}\n".format(validFlag));
    f.write("limits:\n");
    f.write("    memory: {0}\n".format(memLimit));
    # close
    f.close();

def main():
    global pdfPath;
    # input data
    probName  = input("Input Prob Name        : ");
    timeLimit = input("Input Timelimit (    1): "); # "1.5"
    memLimit  = input("Input Memory    ( 62.5): "); # "62.5"
    validFlag = "case_sensitive space_change_sensitive";
    validFlag = input("Input validFlag (exact): ");
    if(validFlag == "exact"): validFlag = "case_sensitive space_change_sensitive";
    # reset
    deleteIt(zipPath);
    # create file
    createIniFile(timeLimit);
    createYamlFile(probName, memLimit, validFlag);
    # check pdf file
    if(not os.path.exists(pdfPath)):
        print("tcframeConv: 'problem.pdf' not found, 'dummy.pdf' will be used instead");
        pdfPath = pdfPathDummy;
    # create zip
    createZip();
    # delete file
    deleteIt(iniPath);
    deleteIt(yamlPath);

main();

# EOF