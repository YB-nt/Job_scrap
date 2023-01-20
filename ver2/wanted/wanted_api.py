
import pandas as pd
import json
from pprint import pprint

from urllib import parse
import simplejson, urllib
import urllib.request

search_keyword =""

def req_get_list(search_keyword):
    target_url = parse.urlparse(f"https://www.wanted.co.kr/api/v4/jobs?&country=kr&job_sort=company.response_rate_order&locations=all&years=-1&query={search_keyword}&limit=100&")
    query = parse.parse_qs(target_url.query)
    url_query = parse.urlencode(query, doseq=True)
    result_url ='https://www.wanted.co.kr/api/v4/jobs?&'+ url_query

    r = simplejson.load(urllib.request.urlopen(result_url))
    
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
        
        locals()[f"r{str(i+1)}"]= req_get_list(v)
        a,b,c,d = split_dict(locals()[f"r{str(i+1)}"],i)

        id_list.extend(a)
        company_name_list.extend(b)
        company_industry_list.extend(c)
        position_list.extend(d)

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

