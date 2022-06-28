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
driver.get("https://www.wanted.co.kr/wd/90288")




dic_job_scarp ={}
list_job_titles = ['AI 엔지니어 (머신러닝 ML/딥러닝 DL)']
job_page = driver.page_source
page_soup = bs(job_page,'html.parser')
section = page_soup.find('section',{"class":"JobDescription_JobDescription__VWfcb"})
dic_job_scarp[list_job_titles[0]]=section.text

print(dic_job_scarp)
driver.quit()