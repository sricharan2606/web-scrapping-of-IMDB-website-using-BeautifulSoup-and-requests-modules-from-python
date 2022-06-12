import pandas as pd
import json
import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"
resp=requests.get(url).content

soup=BeautifulSoup(resp,'html.parser')
titles=soup.find_all('td',class_='titleColumn')
ratings=soup.find_all('strong')
images=soup.find_all('img')
movtitle=[]
movratings=[]
movyear=[]
movimage=[]
movli=[]
for l in titles:
    l1=l.a
    l2=l1.get('href')
    l3="https://www.imdb.com"+l2+"?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=RGNHC807V75ACBF59G2C&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1"
    movli.append(l3)
for img in images:
    imgs=img.get('src')
    movimage.append(imgs)  
for tit in titles:
    t=tit.a.text
    movtitle.append(t)
    year=tit.span.text
    movyear.append(year) 
for i in ratings:
    rate=i.text.strip()
    movratings.append(rate)
data={'link':movli,'images':movimage,'year':movyear,'ratings':movratings}
df=pd.DataFrame(data=data) 
d=json.dumps(data)
l=json.loads(d) 

with open("movies.json",'w') as f:
    f.write(d)
    f.close()