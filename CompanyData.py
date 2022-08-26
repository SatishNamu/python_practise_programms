import lxml.html as htmlparser
htmlData=htmlparser.parse(r'C:\Users\manohar namu\OneDrive\Desktop\satish\CompanyData.html')
headers=[]
CompanysData={}


for hdrs in htmlData.xpath("//tr")[0]:
    headers.append(hdrs.text)

    
for tr in htmlData.xpath("//tr")[1:]:
    CompanysData[tr[0].text]={}
    for hdr in range(1,len(headers)):
        CompanysData[tr[0].text][headers[hdr]]={}
        CompanysData[tr[0].text][headers[hdr]]=tr[hdr].text
        
import pprint        
pprint.pprint(CompanysData)