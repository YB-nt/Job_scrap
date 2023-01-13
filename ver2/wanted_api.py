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

# 잘못된 api를 불러와서 전체 데이터를 수집할수없었다. 
# 새로 찾아서 테스트 해보았다.
def req_get_list(search_keyword):
    target_url = parse.urlparse(f"https://www.wanted.co.kr/api/v4/jobs?&country=kr&job_sort=company.response_rate_order&locations=all&years=-1&query={search_keyword}&limit=100&")
    query = parse.parse_qs(target_url.query)
    url_query = parse.urlencode(query, doseq=True)
    result_url ='https://www.wanted.co.kr/api/v4/jobs?&'+ url_query

    r = simplejson.load(urllib.request.urlopen(result_url))
    # print(len(r['data']))
    return r


def split_dict(dic,i):
    id_list=[]  
    company_name_list =[]
    company_industry_list  =[]
    position_list =[]

    for j in range(0,len(dic['data'])):
        id = dic['data'][j]['id']
        cn = dic['data'][j]['company']['name']
        cin = dic['data'][j]['company']['industry_name']
        pos = dic['data'][j]['position']
    
        id_list.append(id)    
        company_name_list.append(cn)
        company_industry_list.append(cin)
        position_list.append(pos)

    return id_list,company_name_list,company_industry_list,position_list

    


def deduplicatesId_N_makeDf(key_word_list):
    # 동적변수 할당해서 검색할 데이터를 나누어주고 이렇게 불러와준 id를 모아놓고 return 
    id_list=[]
    company_name_list =[]
    company_industry_list  =[]
    position_list =[]
    # opt=1
    
    for i,v in enumerate(key_word_list):
        # print(v)
        locals()[f"r{str(i+1)}"]= req_get_list(v)
        # print(len(locals()[f"r{str(i+1)}"]['jobs']['data']))
        # print("load data")
        a,b,c,d = split_dict(locals()[f"r{str(i+1)}"],i)

        id_list.extend(a)
        company_name_list.extend(b)
        company_industry_list.extend(c)
        position_list.extend(d)

        # 나중에 중복제거하고 저장하는 방식으로 수정 
        # 우선 지금은 무조건 저장 하는 방식으로 수행 
        # if(len(id_list)>0):
        #     if(locals()[f"r{str(i+1)}"]['data'][0]['id'] in id_list):
        #         continue
        #     else:
        #         print("load data")
        #         id_list,company_name_list,company_industry_list,position_list = split_dict(locals()[f"r{str(i+1)}"],i)        
        # else:
        #     print("load data")
        #     id_list,company_name_list,company_industry_list,position_list = split_dict(locals()[f"r{str(i+1)}"],i)
    
    # print(id_list)
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

keyword =["데이터 엔지니어",'데이터엔지니어','data engineer','MLOps']

company_df,search_list = deduplicatesId_N_makeDf(keyword)
# print(search_list)
job_detail = pd.DataFrame(columns=['requirements','preferred_points','main_tasks','intro','benefits'])
for num in search_list:
    job_detail = req_get_jobcard(num,job_detail)


print(company_df)
print(job_detail)



    