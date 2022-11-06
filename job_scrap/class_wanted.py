
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver



class wanted:
    def __init__(self,keyword):
        self.keyword = keyword
        # request_headers = { 'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'), } 
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37')
        self.options.add_argument('headless')
        self.options.add_argument("disable-gpu")
        self.options.add_argument('--start-maximized')
        self.options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=self.options)

        self.base_url1 = "https://www.wanted.co.kr/search?query="
        self.dic_job_scrap = {"job_name":"","job_section":"","link":"","cn_name":""}
        self.dic_job_scarp = {}
        self.job_hrefs=[]
        self.link=[]
        self.cn_list=[]
        self.temp_list_j_name=[]
        self.temp_list_section=[]
        self.temp_list_lnk=[]
        self.temp_list_cname=[]
        self.page_count =0
    

    def scroll_down(self):
        prev_height = self.driver.execute_script("return document.body.scrollHeight")
        # 웹페이지 맨 아래까지 무한 스크롤
        while True:
            # 스크롤을 화면 가장 아래로 내린다
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            # 페이지 로딩 대기
            sleep(0.8)
            # 현재 문서 높이를 가져와서 저장
            curr_height = self.driver.execute_script("return document.body.scrollHeight")
            if(curr_height == prev_height):
                break
            else:
                prev_height = self.driver.execute_script("return document.body.scrollHeight")

    def jobcard(self):
        self.driver.get(self.base_url1+self.keyword)
        sleep(0.5)
        self.scroll_down()

        page1 = self.driver.page_source

        soup=bs(page1, 'html.parser')

        job_cards = soup.findAll("div", {"data-cy": "job-card"})
        for job_card in job_cards:
            temp = job_card.find('a',href=True)['href']
            self.job_hrefs.append(temp)

        return self.job_hrefs

    def job_detail(self):
        job_hrefs=self.jobcard()
        base_url2 ="https://www.wanted.co.kr"

        for job_href in job_hrefs[:len(job_hrefs)]:
            self.page_count+=1
            # print("-"*50)
            # print("Count:",self.page_count)
            # print("-"*50)
            # print(base_url2 + job_href)
            # print("-"*50)
            self.driver.get(base_url2+job_href)

            page = self.driver.page_source
            soup_page = bs(page,"html.parser")
            
            company_name=""
            section=""
            job_title=""
            
            try:        
                job_title = soup_page.find('section',{"class":"JobHeader_className__HttDA"}).find('h2').text
            except:
                job_title ='정보 없음'

            # print(job_title)

            try:
                section = soup_page.find('section',{"class":"JobDescription_JobDescription__VWfcb"}).text
            except:
                job_title ='정보 없음'

            try:
                company_name = soup_page.find('section',{"class":"JobHeader_className__HttDA"}).find('h6').find('a').text
            except:
                job_title ='정보 없음'

            self.temp_list_j_name.append(job_title)
            self.temp_list_section.append(section)
            self.temp_list_lnk.append(str(base_url2 + job_href))
            self.temp_list_cname.append(company_name)
            
        self.dic_job_scrap["job_name"]= self.temp_list_j_name
        self.dic_job_scrap["job_section"]=self.temp_list_section
        self.dic_job_scrap['link'] = self.temp_list_lnk
        self.dic_job_scrap['cn_name'] = self.temp_list_cname

        self.driver.quit()

        df = pd.DataFrame(self.dic_job_scrap)

        # print(df)

        #확인용 csv파일
        # df.to_csv("./bin/job_srcap.csv")

        return df



