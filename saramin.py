import requests as req
from bs4 import BeautifulSoup as soup 
import re

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Whale/3.16.138.27 Safari/537.36'}

# keyword = input("input keyword: ")
keyword='데이터 엔지니어'


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
    """
모집부분 및 상세내용
    공통자격요건
    담당업무 
    지원자격
    우대사항
각 요건들을 나누기 위해서 html 태그를 기준으로 
text 앞의 < 뒤의 > 검색해서 태그 검색 
포함되어있는 태그별로 분류해주기 
ex <tr>담당업무</tr>일때 담당업무 앞의< ~ 뒤의 > 까지 불러오고
첫 <에서 가까운 > 를 찾아서 태그 추출 
해당 tr ~ 다음 tr 나올떄까지 데이터로 분류

    """
    return 



base_url = "https://www.saramin.co.kr"
url_list = make_url_list(keyword=keyword)
total_url = [base_url+add_url for add_url in url_list]
detail_page =[]

test_url = total_url[:4]
# print("-000000000000000000000",len(test_url))

for lnk in test_url:   
    detail_content_num = re.search('rec_idx=(.+?)$',lnk).group(1)
    detail_page.append(f'https://www.saramin.co.kr/zf_user/jobs/relay/view-detail?rec_idx={detail_content_num}&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content=')


# print(detail_page)

for lnk in detail_page:
    # check=0
    resp = req.get(lnk,headers=headers)
    if(resp.status_code==200):
        page_source = soup(resp.text,"html.parser")
        contents = page_source.find('div',class_='wrap_tbl_template')
        # if(contents!=None):
        #     contents= contents.find('table')
        # else:
        #     contents=page_source.find('table',class_="tbl_template")
        if(contents!=None):
            conf = contents.text
            conf_list = conf.split('\n')
            for c in conf_list:
                print(c)
                print('\n'*2)
        # if(contents!=None):
        #     # print(contents.text)
        #     # print('-'*50)
        #     job_part = contents.find('td')
        #     if(job_part!=None):
        #         while(job_part.findNext('tr') != None):  
        #             job_part = job_part.findNext('tr')
        #             # print("*"*100)
        #             job_part_text = job_part.text
        #             if(check==0):
        #                 print('지원자격')
        #                 print(job_part_text)
        #                 print(lnk)
        #                 print('-'*50)
        #             if(check==1):
        #                 print('우대사항')
        #                 print(job_part_text)
        #                 print(lnk)
        #                 print('-'*50)
        #             if(job_part_text=='공통 자격요건'):
        #                 check=1
        #                 continue
        #             if(len(job_part_text)==4):
        #                 if(job_part_text=='지원자격'):
        #                     check=1
        #                     continue
        #                 if(job_part_text=='우대사항'):
        #                     check=2
        #                     continue
        #                 else:
        #                     check=0
        #                     continue
                    
                        

                            
            

# 여러개의 포지션을 구인하는 경우 처리를 해주어야 한다.



    else:
        print(resp.status_code)



