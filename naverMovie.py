from bs4 import BeautifulSoup as bs
import requests

URL = "https://movie.naver.com/movie/running/current.nhn?order=reserve"
response = requests.get(URL)
soup = bs(response.text, 'html.parser')
movieList = soup.select("#content > div.article > div > div.lst_wrap > ul > li")

ent_dict = {}

f = open('naverMovie.txt', 'w', encoding='utf-8')
for movie in movieList:
    temp_dict = {}
    a = movie.select_one("dl > dt > a")
    f.write("{\n")
    f.write(f"\tName : {a.text}\n\tlinkCode : {a['href'][28:]}\n")
    f.write("}\n")
f.close()