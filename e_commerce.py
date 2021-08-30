from ast import dump
import requests
from bs4 import BeautifulSoup
import json
import pprint
url="https://webscraper.io/test-sites"
Res=requests.get(url)
htmlcontent=Res.content
soup=BeautifulSoup(htmlcontent,"html.parser")
div=soup.find('div',class_='container test-sites')
div1=div.find_all('div',class_='col-md-7 pull-right')
def e_commerce():
    list1=[]
    s=1
    details={'postion':s,'name':'','link':''}
    for i in range(0,len(div1)):
        details['name']=div1[i].a.get_text().strip()

        e_commerce_link=div1[i].a['href']
        details['link']="https://webscraper.io"+e_commerce_link
        list1.append(details)
        s+=1
        details={'postion':s,'name':'','link':''}
        # print(details)
    with open('e_commerce.json','w') as j:
        json.dump(list1,j,indent=5)

    return list1

pprint.pprint(e_commerce())