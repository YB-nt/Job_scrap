from time import sleep
from urllib import response
from wsgiref.util import request_uri
from bs4 import BeautifulSoup as bs
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

request_headers = { 
'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'), } 


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument('--start-maximized')
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

base_url1 = "https://www.wanted.co.kr/search?query="
keyword ="딥러닝"

dic_job_scarp = {}
job_hrefs = []


driver.get(base_url1+keyword)
# 스크롤 다운 
# 수정 필요 
def scroll_down():
    prev_height = driver.execute_script("return document.body.scrollHeight")
    # 웹페이지 맨 아래까지 무한 스크롤
    while True:
        # 스크롤을 화면 가장 아래로 내린다
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # 페이지 로딩 대기
        sleep(0.8)
        # 현재 문서 높이를 가져와서 저장
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if(curr_height == prev_height):
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")



sleep(0.5)
scroll_down()

page_count =0
page1 = driver.page_source
soup=bs(page1, 'html.parser')
driver.quit()

job_cards = soup.findAll("div", {"data-cy": "job-card"})
for job_card in job_cards:
    temp = job_card.find('a',href=True)['href']
    job_hrefs.append(temp)
# print(job_hrefs)


base_url2 ="https://www.wanted.co.kr"
for job_href in job_hrefs:
    page_count+=1
    print("-"*50)
    print("Count:",page_count)
    print("-"*50)
    print(base_url2 + job_href)
    print("-"*50)
    response = requests.get(base_url2 + job_href , headers = request_headers)
    if(response.status_code==200):
        soup_page = bs(response.text, 'html.parser')
        job_title = soup_page.find('section',{"class":"JobHeader_className__HttDA"}).find('h2').text
        section = soup_page.find('section',{"class":"JobDescription_JobDescription__VWfcb"}).text
        dic_job_scarp[job_title]=section
    else:
        print("status_code:",response.status_code)

print(list(dic_job_scarp.items()))
