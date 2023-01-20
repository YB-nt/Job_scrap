import scrapy
from urllib import parse
from pprint import pprint

class JobkoreaSpider(scrapy.Spider):
    name = 'jobkorea'
    allowed_domains = ['www.jobkorea.co.kr']

    def start_requests(self):
        search_keyword="데이터 엔지니어"
        target_url = parse.urlparse(f"https://www.jobkorea.co.kr/Search/?stext={search_keyword}")
        query = parse.parse_qs(target_url.query)
        url_query = parse.urlencode(query, doseq=True)
        
        encoding_url = 'https://www.jobkorea.co.kr/Search/?'+ url_query
        urls = [encoding_url]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)
    
    def parse_url(self,response):
        # url_form = "/Recruit/GI_Read/"
        temp =[li.attrib['data-gavirturl'] for li in response.xpath('//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/ul/li')]
        urls = [url.replace('/virtual','') for url in temp]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_url)

    def parse_detail(self, response):
        job_line = [line for line in response.xpath('//*[@id="dev-template-v2-part"]/div/table/tbody/tr/td[2]/td')]
        jobAll = jobAll.append(job_line)

        pprint(jobAll)
        
        
        

        



