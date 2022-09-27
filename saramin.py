from os import linesep
import requests as req
from bs4 import BeautifulSoup as soup 
import re

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Whale/3.16.138.27 Safari/537.36'}

# keyword = input("input keyword: ")
keyword='딥러닝'


def make_url_list(keyword):
    search_base_url = "https://www.saramin.co.kr/zf_user/search?searchword="
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
    
    return url_list

# 2  담당업무,자격요건,우대사항 나누기 
def crawler():
    return 



base_url = "https://www.saramin.co.kr"
url_list = make_url_list(keyword=keyword)
total_url = [base_url+add_url for add_url in url_list]
detail_page =[]

test_url = total_url[:4]

for lnk in test_url:   
    detail_content_num = re.search('rec_idx=(.+?)$',lnk).group(1)
    detail_page.append(f'https://www.saramin.co.kr/zf_user/jobs/relay/view-detail?rec_idx={detail_content_num}&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content=')

for lnk in detail_page:
    resp = req.get(lnk,headers=headers)
    if(resp.status_code==200):
        page_source = soup(resp.text,"html.parser")
        contents = page_source.find('div',class_='wrap_tbl_template').find('td')
        if(contents!=None):
            children = contents.findChildren("table" , recursive=False)
            for child in children:
                print(lnk)
                print('-'*50)
                print(child.text)

# 여러개의 포지션을 구인하는 경우 처리를 해주어야 한다.



    else:
        print(resp.status_code)



