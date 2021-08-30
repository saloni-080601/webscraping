import requests
from bs4 import BeautifulSoup
import json
import pprint

def scrab_top_list():
    url1="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    page=requests.get(url1)
    soup=BeautifulSoup(page.text,'html.parser')
    div=soup.find('div',class_='_1gX7').span.get_text()
   
    var=int(div[1:5])
    
    var1=var//2
    print(var1)
    i=0
    pical_list=[]
    postion=1
    details={'postion':postion,'name':'','rate':'','link':''}
    while i<var1:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(i)
        Res=requests.get(url)
        htmlcontent=Res.content
        soup=BeautifulSoup(htmlcontent,"html.parser")
        main_div=soup.find("div",class_="_3RA-")
        main_div1=main_div.find_all("div",class_="UGUy")
        rate_div=soup.find_all('div',class_='_1kMS')
        # print(rate_div)
        url_div=soup.find_all('div',class_='_3WhJ')

        for j in range(0,len(main_div1)):
            
            details['name']=main_div1[j].get_text()
            details['rate']=rate_div[j].span.get_text()
            pikal_url=url_div[j].a['href']

            details['link']="https://paytmmall.com"+pikal_url
            pical_list.append(details)
            

            details={'postion':postion,'name':'','rate':'','link':''}
            
            postion+=1
            i+=1

            continue

    with open('basic.json','w') as h:
        json.dump(pical_list,h,indent=5)
    
pprint.pprint(scrab_top_list())