import scrapy
from urllib import parse
from pprint import pprint
from scrapy import Selector

class JobkorealnkSpider(scrapy.Spider):
    name = 'jobkorea'
    allowed_domains = ['www.jobkorea.co.kr']
    temp =[]
    def start_requests(self):
        search_keyword="데이터 엔지니어"
        urls =[f"https://www.jobkorea.co.kr/Search/?stext={search_keyword}&tabType=recruit&Page_No={page_num}" for page_num in range(1,6)]
        for url in urls:
            target_url = parse.urlparse(url)
            query = parse.parse_qs(target_url.query)
            url_query = parse.urlencode(query, doseq=True)
            encoding_url = 'https://www.jobkorea.co.kr/Search/?'+ url_query
            yield scrapy.Request(url=encoding_url,callback=self.parse_url)
    
    def parse_url(self,response):
        # url_form = "/Recruit/GI_Read/"
        temp =[li.attrib['data-gavirturl'] for li in response.xpath('//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li')]
        urls = [url.replace('/virtual','') for url in temp]
        
        # print(urls)
        # return urls
        for url in urls:
            target_url = parse.urlparse(url)
            query = parse.parse_qs(target_url.query)
            url_query = parse.urlencode(query, doseq=True)
            encoding_url = url.replace(url[url.find('Oem_Code'):],url_query) 
            print(encoding_url)
            yield scrapy.Request(url=encoding_url,callback=self.parse_detail)

    def parse_detail(self,response):
        # jobkorea 에서는 iframe 안에 데이터가 있기때문에 그냥 지정하면 데이터가 나오지 않는것 같다
        print(response.xpath('//*[@id="gib_frame"]/html/body/div/table/tbody/tr/td/div/div[2]/div[1]/div/table/tbody/tr/td[2]').extract())
        

    

        

    
        
        
        

        



