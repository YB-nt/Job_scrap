import requests
from bs4 import BeautifulSoup as bs
import time
from requests.auth import HTTPBasicAuth

request_headers = { 'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/102.0.1264.37'), } 
page_count=0
job_hrefs=['/wd/35398', '/wd/69475', '/wd/105834', '/wd/56969', '/wd/111904', '/wd/111902', '/wd/71968', '/wd/57696', '/wd/63936', '/wd/82150', '/wd/69472', '/wd/83631', '/wd/90288', '/wd/19529', '/wd/114542', '/wd/103663', '/wd/104840', '/wd/118307', '/wd/105502', '/wd/29701', '/wd/98950', '/wd/114923', '/wd/114950', '/wd/96823', '/wd/39278', '/wd/45157', '/wd/56817', '/wd/101290', '/wd/84963', '/wd/111172', '/wd/104027', '/wd/118396', '/wd/108103', '/wd/98019', '/wd/96845', '/wd/106850', '/wd/94077', '/wd/114823', '/wd/76066', '/wd/110569', '/wd/21479', '/wd/113049', '/wd/95932', '/wd/107416']
base_url2 ="https://www.wanted.co.kr"
for job_href in job_hrefs:
    page_count+=1
    print("-"*50)
    print("Count:",page_count)
    print("-"*50)
    print(base_url2 + job_href)
    print("-"*50)
    job_url =base_url2 + job_href
    response = requests.get( job_url, headers = request_headers,allow_redirects=True)
    if(response.status_code==200):
        time.sleep(1)
        soup_page = bs(response.content, 'html.parser')
        
        test = soup_page.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb')
        print(test)
        # job_title = soup_page.find('section',{"class":"JobHeader_className__HttDA"}).find('h2').text
        # section = soup_page.find('section',{"class":"JobDescription_JobDescription__VWfcb"}).text
        # dic_job_scarp[job_title]=section
    else:
        print("status_code:",response.status_code)
    if(page_count>1):
        break
