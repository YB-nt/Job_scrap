import requests as req
from bs4 import BeautifulSoup as soup 


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Whale/3.16.138.27 Safari/537.36'}
search_base_url = "https://www.saramin.co.kr/zf_user/search?searchword="
keyword = input("찾아볼 키워드: ")

add_url = search_base_url+keyword
resp = req.get(add_url,headers=headers)
url_list = []

if(resp.status_code==200):
    page_source = soup(resp.text,"html.parser")
    contents = page_source.find("div",class_='content')
    # h2 class : job_tit
    job_title = contents.find_all("h2",class_="job_tit")
    for lnk in job_title:
        url_list.append(lnk.find('a',href=True)['href'])
else:
    print(resp.status_code)
    

# 2  담당업무,자격요건,우대사항 나누기 
base_url = "https://www.saramin.co.kr"
total_url = [base_url+add_url for add_url in url_list]
print(total_url)


