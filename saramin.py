import requests as req
from bs4 import BeautifulSoup as soup 
import re
import time
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Whale/3.16.138.27 Safari/537.36'}

keyword = input("input keyword: ")
# keyword=''


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

def make_df():
    df = pd.DataFrame(columns=['url','html'])
    return df

def scraper():
    base_url = "https://www.saramin.co.kr"
    url_list = make_url_list(keyword=keyword)
    total_url = [base_url+add_url for add_url in url_list]
    detail_page =[]

    for lnk in total_url:   
        detail_content_num = re.search('rec_idx=(.+?)$',lnk).group(1)
        detail_page.append(f'https://www.saramin.co.kr/zf_user/jobs/relay/view-detail?rec_idx={detail_content_num}&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content=')

    access_page = []
    access_link = []
    for lnk in detail_page:
        # check=0
        resp = req.get(lnk,headers=headers)
        if(resp.status_code==200):
            page_source = soup(resp.text,"html.parser")
            contents = page_source.find('div',class_='wrap_tbl_template')
            if(contents!=None):
                access_page.append(contents)
                access_link.append(lnk)
        else:
            print(resp.status_code)

    return access_link,access_page




df = make_df()
lnk,page = scraper()

df.html=page
df.url=lnk
file_name=str(time.time()).replace('.','_')
df.to_csv(f'.{file_name}.csv',index=True)
