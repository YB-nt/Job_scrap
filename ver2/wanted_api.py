"""
기존에 requests를 사용해서 데이터를 불러오려고 하였으나, 
인코딩 문제가 있어서 urllib로 대체하였다. 
# https://velog.io/@jklbnm2021/requests-%EC%93%B0%EB%A0%A4%EB%8A%94%EB%8D%B0-latin-1i-error-%EA%B0%80-%EB%9C%A8%EB%A9%B4%EC%84%9C-%EC%8A%A4%ED%81%AC%EB%9E%A9%ED%95%91%EC%9D%B4-%EC%95%88-%EB%90%9C%EB%8B%A4.-%EC%9A%B0%EC%A7%A4%EA%BC%AC
    # r = requests.get(result_url,data={"sameAddressGroup":"false"},\
    #         headers={
    #             "vary": "Accept-Encoding",
    #             "Accept-Encoding": "gzip",
    #             "Referer":f"https://www.wanted.co.kr/search?query={search_keyword}",
    #             "Sec-Fetch-Dest":"empty",
    #             "Sec-Fetch-Mode":"cors",
    #             "Sec-Fetch-Site":"same-origin",
    #             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    #             "wanted-user-agent": "user-web",
    #             "wanted-user-country": "KR",
    #             "wanted-user-language": "ko"
    #             })
    
    # r = request.urlopen(result_url)
    # temp=json.loads(r.text)

"""

# <job_card를 불러오기 위해서 필요 >
# job_card_list


import pandas as pd
import json
from pprint import pprint

from urllib import parse
import simplejson, urllib
import urllib.request

search_keyword =""

def req_get_list(search_keyword):
    target_url = parse.urlparse(f"https://www.wanted.co.kr/api/v4/search/summary?&locations=all&job_sort=company.response_rate_order&years=-1&country=kr&query={search_keyword}")
    query = parse.parse_qs(target_url.query)
    url_query = parse.urlencode(query, doseq=True)
    result_url ='https://www.wanted.co.kr/api/v4/search/summary?&'+ url_query

    r = simplejson.load(urllib.request.urlopen(result_url))


    return r

def make_company_info(r):
    id_list =[]
    
    

    for i in r['jobs']['data']:
        id_list.append(i['id'])
        company_name_list.append(i['company']['name'])
        company_industry_list.append(i['company']['industry_name'])
        position_list.append(i['position'])

    #position info dataframe
    

    return df,id_list
def binary_search_id_list(value,id_list):
    sorted_id_list  = id_list.sort()
    start = 0
    last = len(sorted_id_list)
    while(start<=last):
        if(id_list[last//2] ==value):
            return int(0)
        if(id_list[last//2]>value):
            last=id_list[last//2]-1
        else:
            start = id_list[last//2]+1
    return int(1)


def deduplicatesId_N_makeDf(key_word_list):
    # 동적변수 할당해서 검색할 데이터를 나누어주고 이렇게 불러와준 id를 모아놓고 return 
    id_list=[]
    company_name_list =[]
    company_industry_list  =[]
    position_list =[]
    for i,v in enumerate(key_word_list):
        locals()[f"r{str(i+1)}"]= req_get_list(v)
        if(id_list!=0):
            opt = binary_search_id_list(locals()[f"r{str(i+1)}"],id_list)

        if(opt==1):
            id_list.append(locals()[f"r{str(i+1)}"]['jobs']['data']['id'])    
            company_name_list.append(locals()[f"r{str(i+1)}"]['jobs']['data']['company']['name'])
            company_industry_list.append(locals()[f"r{str(i+1)}"]['jobs']['data']['company']['industry_name'])
            position_list.append(locals()[f"r{str(i+1)}"]['jobs']['data']['position'])
        else:
            continue
    
    df = pd.DataFrame()
    df['id'] = id_list 
    df['company_name'] = company_name_list
    df['company_industry_name'] = company_industry_list
    df['position'] = position_list

    return df,id_list

def req_get_jobcard(card_num,df):
    job_card_url ='https://www.wanted.co.kr/api/v4/jobs/'+str(card_num)

    r = simplejson.load(urllib.request.urlopen(job_card_url))

    benefits = r['job']['detail']['benefits']
    intro = r['job']['detail']['intro']
    main_tasks = r['job']['detail']['main_tasks']
    preferred_points = r['job']['detail']['preferred_points']
    requirements = r['job']['detail']['requirements']

    # row 데이터 저장
    df.loc[df.shape[0]-1] = [requirements,preferred_points,main_tasks,intro,benefits]
    
    return df




# job card 상세 내용
card_num = ''




keyword =["데이터 엔지니어",'데이터엔지니어','data engineer','MLOps']

df,search_list = deduplicatesId_N_makeDf(keyword)
job_detail = pd.DataFrame(columns=['requirements','preferred_points','main_tasks','intro','benefits'])
for num in search_list:
    job_detail = req_get_jobcard(num,job_detail)
    
print(job_detail)



    