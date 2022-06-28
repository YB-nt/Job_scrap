from time import sleep
from bs4 import BeautifulSoup as bs
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument('--start-maximized')
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

base_url = "https://www.wanted.co.kr/search?query="
keyword ="딥러닝"

dic_job_scarp = {}

driver.get(base_url+keyword)
# 스크롤 다운 
# 수정 필요 
for i in range(0,10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)
page_count =0
page1 = driver.page_source
soup=bs(page1, 'html.parser')
# print(soup)
job_titles = soup.findAll("div", {"class": "job-card-position"})
for job_title in job_titles:
    # print(job_title.text)
    # list_job_titles.append(job_title.text)
    page_count +=1

driver.refresh()
sleep(0.5)
# print(list_job_titles)
print("-"*50)
print("job_pages :",page_count)
print("-"*50)
for i in range(1,page_count+1):
    print("-"*50)
    print("Count:",i)
    print("-"*50)
    count =0
    page = f'/html/body/div[1]/div[4]/div[2]/div/div/div[2]/ul/li[{i}]/div/a'
    while True:
        count+=100
        try:
            sleep(0.3)
            driver.find_element_by_xpath(page).click()
            break
        except:
            driver.execute_script(f"window.scrollTo(0, {count});")
            # print(count)

    sleep(0.5)
    job_page = driver.page_source
    page_soup = bs(job_page,'html.parser')
    job_title = page_soup.find('section',{"class":"JobHeader_className__HttDA"}).find('h2').text
    section = page_soup.find('section',{"class":"JobDescription_JobDescription__VWfcb"}).text
    dic_job_scarp[job_title]=section

    driver.back()

print(dic_job_scarp)




driver.quit()