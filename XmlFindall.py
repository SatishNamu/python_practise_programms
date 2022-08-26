import re
import pprint
#Readingfile
xmlread = open(r'C:\Users\manohar namu\OneDrive\Desktop\satish\xmlbookdata.txt')
xmlLines = xmlread.readlines()

BookData = {}

BookID = re.findall('<book id=(.*?)>(.*?)</book>',''.join(xmlLines),re.S)
pprint.pprint(BookID)

for i in range(len(BookID)):
        
    BookData[BookID[i][0]] = {}
    OtherDetails = re.findall('<(.*?)>(.*?)<.*?>',''.join(BookID[i][1]),re.S)
    for j in range(len(OtherDetails)):
        BookData[BookID[i][0]][OtherDetails[j][0]]= OtherDetails[j][1]
   
pprint.pprint(BookData)