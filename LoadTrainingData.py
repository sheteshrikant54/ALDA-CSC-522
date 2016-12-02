import codecs
import re
import csv
from os import walk, path
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from stemming.porter2 import stem

stops = set(stopwords.words("english"))

def getfilelist(dirPathTemp, fileList):
    for (dirpath, dirnames, filenames) in walk(dirPathTemp):
        for filename in filenames:
            fileList.append(path.join(dirpath, filename))


def getimpwords(category, fileList, wr):
    for file in fileList:
        try:
            f = codecs.open(file, 'r')
            # f = codecs.open("D:/MS/ALDA CSC 522/Project/dataDept.csv",'r')
            r = f.read()
            f.close()
        except:
            print(str.encode(file,'ascii',"replace"))
        # print(words)
        soup = BeautifulSoup(r, "lxml")
        letters_only = re.sub("[^a-zA-Z]",  # The pattern to search for
                              " ",  # The pattern to replace it with
                              soup.get_text())  # The text to search
        # print(letters_only)
        lower_case = letters_only.lower()  # Convert to lower case
        words = lower_case.split()
        # print(words)
        meaningful_words = [stem(w) for w in words if not w in stops]
        # print(meaningful_words)
        wr.writerow(category + [' '.join(meaningful_words)])


dirPath1=u"D:/MS/ALDA CSC 522/Project/webkb-data.gtar/webkb-data/webkb/course/training"
dirPath2=u"D:/MS/ALDA CSC 522/Project/webkb-data.gtar/webkb-data/webkb/department/training"
dirPath3=u"D:/MS/ALDA CSC 522/Project/webkb-data.gtar/webkb-data/webkb/faculty/training"
dirPath4=u"D:/MS/ALDA CSC 522/Project/webkb-data.gtar/webkb-data/webkb/other/training"
dirPath5=u"D:/MS/ALDA CSC 522/Project/webkb-data.gtar/webkb-data/webkb/project/training"
dirPath6=u"D:/MS/ALDA CSC 522/Project/webkb-data.gtar/webkb-data/webkb/staff/training"
dirPath7=u"D:/MS/ALDA CSC 522/Project/webkb-data.gtar/webkb-data/webkb/student/training"


fileList1 = []
getfilelist(dirPath1, fileList1)
fileList2 = []
getfilelist(dirPath2, fileList2)
fileList3 = []
getfilelist(dirPath3, fileList3)
fileList4 = []
getfilelist(dirPath4, fileList4)
fileList5 = []
getfilelist(dirPath5, fileList5)
fileList6 = []
getfilelist(dirPath6, fileList6)
fileList7 = []
getfilelist(dirPath7, fileList7)

cat=["category","ImpWords"]

f1 = open('D:/MS/ALDA CSC 522/Project/training.csv', 'wt',newline="")
wr1 = csv.writer(f1, quoting=csv.QUOTE_NONE)
wr1.writerow(cat)

deptCategory = ["course"]
getimpwords(deptCategory, fileList1, wr1)
deptCategory = ["department"]
getimpwords(deptCategory, fileList2, wr1)
deptCategory = ["faculty"]
getimpwords(deptCategory, fileList3, wr1)
deptCategory = ["other"]
getimpwords(deptCategory, fileList4, wr1)
deptCategory = ["project"]
getimpwords(deptCategory, fileList5, wr1)
deptCategory = ["staff"]
getimpwords(deptCategory, fileList6, wr1)
deptCategory = ["student"]
getimpwords(deptCategory, fileList7, wr1)