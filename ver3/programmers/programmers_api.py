import requests
import json
import ast
from bs4 import BeautifulSoup

headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39"}


def job_category_ids_search(target_name):
    """
    "서버/백엔드", "프론트엔드", "웹 풀스택", "안드로이드", "iOS", "머신러닝", "인공지능(AI)", "데이터 엔지니어링", "DBA", "모바일 게임", "게임 클라이언트", "게임 서버", "시스템/네트워크", "시스템 소프트웨어", "데브옵스", "인터넷 보안", "임베디드 소프트웨어", "로보틱스 미들웨어", "QA", "사물인터넷(IoT)", "응용 프로그램", "블록체인", "개발PM", "웹 퍼블리싱", "크로스 플랫폼", "VR/AR/3D", "ERP", "그래픽스"
     중 선택
    """
    ctg = requests.get('https://career.programmers.co.kr/api/job_positions/job_categories')
    if(ctg.status_code == 200):
        # print(ctg.content.decode('utf-8'))
        id_lst = ast.literal_eval(ctg.content.decode('utf-8'))
        
        result = [d for d in id_lst if d['name'] == target_name]

        return result[0]['id']

def job_category_select(l):
    add_url =""
    base_url ='job_category_ids='
    for v in l:
        if(v=='0' or v==0):
            return f"{base_url}0"
        id=job_category_ids_search(v)
        add_url=f"{add_url}{base_url}{id}"

    return add_url


# 0을 선택하면 전체 공고를 확인할수 있다.

# target_name = ["서버/백엔드", "프론트엔드", "웹 풀스택",0]
# print(job_category_select(target_name))


 

url = "https://career.programmers.co.kr/job?page=1&order=recent&job_category_ids=0"
requests.get(url,headers=headers)

    