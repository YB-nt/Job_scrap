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
keyword =""

driver.get(base_url+keyword)
for i in range(0,10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)

req = driver.page_source
soup=bs(req, 'html.parser')
# print(soup)
job_titles = soup.findAll("div", {"class": "job-card-position"})
for job_title in job_titles:
    print(job_title.text)
    print("--")

driver.quit()