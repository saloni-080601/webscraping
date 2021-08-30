import requests
from bs4 import BeautifulSoup
import json
import pprint
url="https://www.imdb.com/india/top-rated-indian-movies/"
Res=requests.get(url)

# print(Res.text)
htmlcontent=Res.content
soup=BeautifulSoup(htmlcontent,"html.parser")
def scrab_top_list():
    main_div=soup.find('div', class_='lister')
    tbody=main_div.find('tbody',class_='lister-list')
    trs=tbody.find_all('tr')
    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_url=[]
    movie_ratings=[]
    for tr in trs:
        postion=tr.find('td',class_='titleColumn').get_text().strip()
        rank=''
        for i in postion:
            if '.' not in i:
                rank=rank+i
        movie_ranks.append(rank)
        title=tr.find('td',class_='titleColumn' ).a.get_text()
        movie_name.append(title)
        year=tr.find('td',class_="titleColumn").span.get_text()
        year_of_realease.append(year)
        imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)
        link=tr.find('td',class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com" + link
        movie_url.append(movie_link)
    Top_movies = []
    details={'postion':'','name':'','year':'','rating':'','url':''}
    for i in range(0,len(movie_ranks)):
        details['postion']=movie_ranks[i]
        details['name']=str(movie_name[i])
        details['year']=int(year_of_realease[i][1:5])
        details['rating']=float(movie_ratings[i])
        details['url']=movie_url[i]
        Top_movies.append(details)
        details={'postion':'','name':'','year':'','rating':'','url':''}
    with open ('postion.json',"w") as u:
        json.dump(Top_movies,u,indent=5)    
    return (Top_movies)

scrabbed=(scrab_top_list()) 

def group_of_year(movies):
    
    year=[]
    dict1={}
    for i in movies:
        if i['year'] not in year:
            year.append(i['year'])
    for j in year:
        list1=[]
        for k in movies:
            if j==k['year']:
                list1.append(k)
            dict1.update({j:list1})
    with open ('web.json',"w") as u:
        json.dump(dict1,u,indent=5)
    return dict1
    

    
dec=group_of_year(scrabbed)

def group_of_dec(movies):
    list1=[]
    moviedec={}
    for i in movies:
        some=i%10
        decade=i-some
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for j in moviedec:
        dec1=j+9   
        list2=[] 
        for k in movies:
            if k<=dec1 and k>=j:
                for x in movies[k]:
                    moviedec[j].append(x)
    with open ('scrab.json',"w") as u:
        json.dump(moviedec,u,indent=5)
    return(moviedec)
pprint.pprint(group_of_dec(dec))
