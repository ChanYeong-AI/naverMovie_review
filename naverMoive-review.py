from bs4 import BeautifulSoup as bs
import requests

URL = "https://movie.naver.com/movie/running/current.nhn?order=reserve"
response = requests.get(URL)
soup = bs(response.text, 'html.parser')
movieList = soup.select("#content > div.article > div > div.lst_wrap > ul > li")


movie_code_list = []
for movie in movieList:
    a = movie.select_one("dl > dt > a")
#     a.text
    movie_code_list.append(a['href'][28:])
    
URL_head = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code="
URL_tail = "&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"
    
    #_filtered_ment_i
    
score = []    

f = open('naverMovieReview.csv', 'w', encoding='utf-8')
f.write("score,review\n")
    
for code in movie_code_list:
    URL = URL_head + code + URL_tail
# URL = URL_head + movie_code_list[1] + URL_tail
    response = requests.get(URL)
    soup = bs(response.text, 'html.parser')
    ul = soup.select("div.score_result > ul > li")
    rev_id = "#_filtered_ment_"
    j=0

    # ul[1].select_one("a")#['data-src']
    for li in ul:
        rv_soup = li.select_one(rev_id + str(j))
    #     print(rv_soup.select_one())
        if rv_soup.select_one("span"):
            review = rv_soup.select_one("a")['data-src']
        else:
            review = li.select_one(rev_id + str(j)).text.strip()
    #         review = "NO"
        score = li.select_one(".star_score > em").text
        f.write(score+","+review+"\n")
        j += 1


    

f.close()