import scrapy
from scrapy.http import Request
from wanted.items import WantedItem
from wanted.pipelines import WantedPipeline
from pprint import pprint
from datetime import datetime
import logging,json


class JobSpider(scrapy.Spider):
    name = "wanted"
    
    search_keyword =["데이터 엔지니어",'데이터엔지니어','data engineer','MLOps']
    start_urls = [f"https://www.wanted.co.kr/api/v4/jobs?&country=kr&job_sort=company.response_rate_order&locations=all&years=-1&query={keyword}&limit=100&" for keyword in search_keyword]

    now = str(datetime.now().strftime('%Y_%m_%d_%H%M%S'))
        
    logging.basicConfig(filename=f'./log/{now}.log', level=10)

    def __init__(self):
        self.id = ""
        self.base_url = "https://www.wanted.co.kr/api/v4/jobs/"
        self.item = WantedItem()

    def parse(self, response):
        # get id value 
        json_response = json.loads(response.text)
        for j in range(0,len(json_response['data'])):
            
            logging.info(f"ID :{self.id}")
            
            self.id  = json_response['data'][j]['id']
            self.item['id'] = self.id 

            detail_View_url = self.base_url+str(self.id)
            yield Request(url=detail_View_url,callback=self.detail_parse)


    def detail_parse(self, response):
       r = json.loads(response.text)
     
       logging.info(f"Searching URL ::{response.url}")
       
       self.item['담당업무'] =r['job']['detail']['main_tasks']
       self.item['우대사항'] =r['job']['detail']['benefits']
       self.item['자격요건'] =r['job']['detail']['requirements']
       yield self.item       

        



        