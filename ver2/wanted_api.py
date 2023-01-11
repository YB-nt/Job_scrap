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
    # headers={"Accept-Encoding": "gzip",
    #         "Referer":f"https://www.wanted.co.kr/wd/{card_num}",
    #         "Sec-Fetch-Dest":"empty",
    #         "Sec-Fetch-Mode":"cors",
    #         "Sec-Fetch-Site":"same-origin",
    #         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    #         "wanted-user-agent": "user-web",
    #         "wanted-user-country": "KR",
    #         "wanted-user-language": "ko"
    #         }

    r = simplejson.load(urllib.request.urlopen(result_url))

    id_list =[]
    for i in r['jobs']['data']:
        id_list.append(i['id'])
        
    return id_list
  

"""
Request URL: https://www.wanted.co.kr/api/v4/jobs/132286?1672842062478
Request Method: GET
Status Code: 200 
Remote Address: 3.37.165.4:443
Referrer Policy: strict-origin-when-cross-origin

content-encoding: gzip
content-type: application/json
date: Wed, 04 Jan 2023 14:21:00 GMT
server: nginx/1.21.3
vary: Accept-Encoding
x-wanted-expire-time: 2023-01-04T23:22:00
x-wanted-simsmode: 0

:authority: www.wanted.co.kr
:method: GET
:path: /api/v4/jobs/132286?1672842062478
:scheme: https
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
cache-control: no-cache
cookie: uuid=6eee-557a-1d51-4f0e; _fbp=fb.2.1649868403284.1580125321; ab.storage.deviceId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%227ed7f65d-816b-57ff-2971-49ad076c9d5e%22%2C%22c%22%3A1649868402944%2C%22l%22%3A1672831834688%7D; ab.storage.userId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%222448754%22%2C%22c%22%3A1649868762578%2C%22l%22%3A1672831834689%7D; _gcl_aw=GCL.1672831835.Cj0KCQiA5NSdBhDfARIsALzs2EAbdeK3eWmObVuBJatWM3Xzh9bkhS8BbIdbwE1GLMlhML793bgh96kaApFQEALw_wcB; _gcl_au=1.1.28919825.1672831835; _gid=GA1.3.15021600.1672831836; ln_or=eyIyNDM1NzEiOiJkIn0%3D; _gac_UA-62498866-1=1.1672831838.Cj0KCQiA5NSdBhDfARIsALzs2EAbdeK3eWmObVuBJatWM3Xzh9bkhS8BbIdbwE1GLMlhML793bgh96kaApFQEALw_wcB; utm=; ab.storage.sessionId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%2205bb1f0f-c53c-361f-7e6e-8b7d8e18f46a%22%2C%22e%22%3A1672834933038%2C%22c%22%3A1672831834687%2C%22l%22%3A1672833133038%7D; wcs_bt=s_133d2f67e287:1672833133; _ga=GA1.3.1040617207.1649868403; _ga_PE7NVFHKS3=GS1.1.1672833227.1.1.1672833241.0.0.0; _gat_UA-62498866-1=1; _dc_gtm_UA-62498866-1=1; _ga_4XX1N5VVJ2=GS1.1.1672842026.14.1.1672842044.0.0.0; _ga_YKFMYZ2YXR=GS1.1.1672842026.14.1.1672842044.0.0.0; _ga_JMVHE9R721=GS1.1.1672842026.2.1.1672842044.0.0.0; _dd_s=rum=2&id=f2da1d2d-21eb-4c38-9659-6d387c11f9d5&created=1672842016688&expire=1672842962252; amp_d08dcd=ZHFbVWVeEpAvwesLDrHwzJ...1gluif6tn.1gluigadk.2k.1u.4i; AWSALBTG=7KFptpbN4D+ouZSH7UG21I6QmV50QDLFKx3vhrCOJPJpRlLyNFHv/kjdBc2nesvuVKrEC/doQEN5h1shDLD2WbqaQ+N363i63xUI8VAV2j+2uQQdthkkBWR9MGIkk2H7qNSXKJMiOPlVY7vCONUvwMC5dBfx3cOQXAUgVucl6hTE1pKgMfc=; AWSALBTGCORS=7KFptpbN4D+ouZSH7UG21I6QmV50QDLFKx3vhrCOJPJpRlLyNFHv/kjdBc2nesvuVKrEC/doQEN5h1shDLD2WbqaQ+N363i63xUI8VAV2j+2uQQdthkkBWR9MGIkk2H7qNSXKJMiOPlVY7vCONUvwMC5dBfx3cOQXAUgVucl6hTE1pKgMfc=; AWSALB=dOIPdT12clYuCOppt3bF3CiGPE115tknnWFgWiBXgnBGRLMz9XmnVcapykFjZyHsh/5CI+o8VZuouuaL0zBBB27d6LRzv2MRFL1cUbpqQsqpj4jIZ45ed84c985N; AWSALBCORS=dOIPdT12clYuCOppt3bF3CiGPE115tknnWFgWiBXgnBGRLMz9XmnVcapykFjZyHsh/5CI+o8VZuouuaL0zBBB27d6LRzv2MRFL1cUbpqQsqpj4jIZ45ed84c985N
referer: https://www.wanted.co.kr/wd/132286
sec-ch-ua: "Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Whale/3.18.154.7 Safari/537.36
wanted-user-agent: user-web
wanted-user-country: KR
wanted-user-language: ko
"""

# job card 상세 내용
card_num = ''




def req_get_jobcard(card_num):
    job_card_url ='https://www.wanted.co.kr/api/v4/jobs/'+str(card_num)


    # header={"Accept-Encoding": "gzip",
    #         "Referer":f"https://www.wanted.co.kr/wd/{card_num}",
    #         "Sec-Fetch-Dest":"empty",
    #         "Sec-Fetch-Mode":"cors",
    #         "Sec-Fetch-Site":"same-origin",
    #         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    #         "wanted-user-agent": "user-web",
    #         "wanted-user-country": "KR",
    #         "wanted-user-language": "ko"}
    r = simplejson.load(urllib.request.urlopen(job_card_url))

    return r


def make_id_list(key_word_list):
    # 동적변수 할당해서 검색할 데이터를 나누어주고 이렇게 불러와준 id를 모아놓고 return 
    for i,v in enumerate(key_word_list):
        locals()[f"r{str(i+1)}"]= req_get_list(v)
    
    

    # temp = [locals()[f"r{str(i)}"] for i in range(1,len(key_word_list)+1)]
    temp =[]
    for i in range(1,len(key_word_list)+1):
        temp.append(locals()[f"r{str(i)}"])

    id_list =[]
    for i in temp:
        id_list.extend(i)

    id_list = list(set(id_list))

    return id_list


keyword =["데이터 엔지니어",'데이터엔지니어','data engineer','MLOps']

search_list = make_id_list(keyword)

for num in search_list[:3]:
    pprint(req_get_jobcard(num)['job']['detail'])



    