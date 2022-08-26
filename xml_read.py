import re
import pprint

BooksDataFile = open(r"C:\Users\manohar namu\OneDrive\Desktop\satish\xmlbookdata.txt","r")
BooksDataline = BooksDataFile.readlines()  # list of all lines

BookData = {}
bookID = ''
flag = 0 
for eachline in BooksDataline:
    stripped_line = eachline.strip()     # trimmed lines
    
#forbookid    
    
    regex_output1 = re.search(r'<book id=(.*)>', stripped_line)   #bookid
    if regex_output1 is not None:
        bookID = regex_output1.group(1)
        BookData[bookID] = {}
        
#forBookDetails        

    regex_output2 = re.search(r'<(.*)>(.*)<.*>', stripped_line)           
    if regex_output2 is not None:
       BookData[bookID][regex_output2.group(1)] = regex_output2.group(2)
       
#forDescriptionlines0&1 
    
    regex_output3 = re.search(r'<description(|1)(.*)',stripped_line)  
    regex_output4 = re.search(r'(.*)</(description(|1))>',stripped_line)
    
    
    if regex_output3 is not None:
        DescriptionLines = regex_output3.group(2)
        flag = 1
        continue
        
    if regex_output4 is not None:
        DescriptionLines += regex_output4.group(1)
        
        BookData[bookID][regex_output4.group(2)] = DescriptionLines
        flag = 0
        
    if flag == 1:
        DescriptionLines += stripped_line

