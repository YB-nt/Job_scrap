import requests as req
from bs4 import BeautifulSoup as soup 
import re
import time
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Whale/3.16.138.27 Safari/537.36'}

# keyword = input("input keyword: ")
keyword='데이터 엔지니어'

# test
def make_url_list(keyword):
    search_base_url = "https://www.saramin.co.kr/zf_user/search?searchword="
    add_url = search_base_url+keyword
    for page_num  in range(1,5):
        update_url=f"{add_url}&recruitPage={page_num}"
        resp = req.get(update_url,headers=headers)
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
    print(len(url_list))
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

    # test_page = detail_page[:10]
    access_page = []
    except_page = []
    access_link = []
    # print(detail_page)
    for lnk in detail_page:
        resp = req.get(lnk,headers=headers)
        if(resp.status_code==200):
            page_source = soup(resp.text,"html.parser")

            contents = page_source.find('div',class_='wrap_tbl_template')
            if(contents!=None):
                page_text = contents.text
                access_page.append(page_text)
                access_link.append(lnk)
            else:
                contents=page_source.find('div',class_='user_content')
                if(contents!=None):
                    page_text=contents.text
                    access_page.append(page_text)
                    access_link.append(lnk)
                else:
                    except_page.append(lnk)
        else:
            print(resp.status_code)

    
def data_scaling(page_text):
    if(page_text.find("공통 자격요건") != -1):
        if("공통 자격요건" in page_text):
            if(")" in page_text[page_text.find("공통 자격요건")+7:30]):
                common = page_text[page_text.find("공통 자격요건")+7:page_text.find("년)")+2]
            else:
                common = page_text[page_text.find("공통 자격요건")+7:page_text.find("관")+1]
                if("대졸 이상 (4년)S/W F/W 엔지니어S/W팀 0명담당업무" in page_text): 
                    # 특정공고 1개에서 에러 발생...
                    # 이유를 찾지못해서 string 으로 예외처리
                    common = page_text[page_text.find("공통 자격요건")+7:page_text.find("년)")+2]
                else:
                    pass
    page_text = page_text[len("공통 자격요건")+len(common):]
    if("자격요건" in page_text):
        require = page_text[page_text.find('자격요건')+5:page_text.find("우대")]
    elif("지원자격" in page_text):
        require = page_text[page_text.find('지원자격')+5:page_text.find("우대")]

    require = require.replace("\n","")
    require = require.replace("            ㆍ기타 필수 사항","")
    require = require.replace("및","없음")

    if(page_text.find("데이터 엔지니어") !=-1):
        lenght = len("데이터 엔지니어")
        page_text = page_text[page_text.find("데이터 엔지니어")+lenght:]
    elif(page_text.find("data engineer") != -1):
        lenght = len("data engineer")
        page_text = page_text[page_text.find("data engineer")+lenght:]
    else:
        pass
    
    if("담당업무" not in page_text):
        job_main ="정보 없음"
    else:
        job_main = page_text[page_text.find('담당업무')+5:page_text.find("자격")]
        if("우대" in job_main):
            job_main = page_text[page_text.find("담당업무")+5:page_text.find("우대")]

    if(len(job_main)<4):
        job_main = "정보없음"
    




def data_init():
    # 클라우드 데이터 베이스와 연결 
    # 데이터 베이스 먼저 정의 되어있는지 확인 
    # RETURN DATABASE
    pass

def data_load():
    # 데이터 적재 part
    # 원티드 등 다른 사이트의 데이터를 저장하기 위해서 
    # 저장된 데이터베이스에 추가적으로 저장할수 있도록 만들어주기 
    pass




# df = make_df()
# lnk,page = scraper()
scraper()
# df.html=page
# df.url=lnk
# file_name=str(time.time()).replace('.','_')
# df.to_csv(f'.{file_name}.csv',index=True)