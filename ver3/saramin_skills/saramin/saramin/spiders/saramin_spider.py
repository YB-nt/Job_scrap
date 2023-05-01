import scrapy
from scrapy.http import Request
from saramin.items import SaraminItem,SaraminItem_info
from saramin.pipelines import SaraminPipeline
import re,copy
# from pprint import pprint
from datetime import datetime
from functools import reduce
import logging


class JobSpider(scrapy.Spider):
    name = "saramin"
    start_urls = [
        "https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=recently&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4"
    ]
    now = str(datetime.now().strftime('%Y_%m_%d_%H%M%S'))
        
    logging.basicConfig(filename=f'{now}.log', level=logging.INFO)

    def __init__(self):
        pass

    def parse(self, response):
        item = SaraminItem()
        a_job_tits = response.xpath('//h2[@class="job_tit"]')
        for a_job_tit in a_job_tits:
            job_num = a_job_tit.xpath('./a/@href').get()
            extract_num = re.findall(r'(?<=rec_idx=)[0-9]+',job_num)[0]
            item['job_num'] = extract_num
            item['summary_link'] = f'https://www.saramin.co.kr/zf_user/jobs/relay/view-detail?rec_idx={extract_num}&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content='
            yield Request(url=item['summary_link'],callback=self.datail_parse)
            yield item

    def datail_parse(self, response):
        logging.info(f"Searching URL ::{response.url}")
        text = response.xpath("//table[@class='cont_recruit_template']//text()").getall()
        if(len(text)==0):
            text=response.xpath("/html/body/div/div/div[3]/div[2]//text()").getall()
        if(len(text)==0):
            text =response.xpath("(//div[@class='user_content']//dl)[2]//text()").getall()

        if(len(text)!=0):
            if(type(text)==list):
                text = ', '.join(text)
            

        yield self.preprocess(text)
        
    def preprocess(self, text):
        item = SaraminItem_info()
        cp_text = copy.deepcopy(text)
        if cp_text is not None:
            text = str(cp_text)
            text = re.sub(r'[^\w\s-]', '', text)
            regex = re.compile(r'자격요건|우대사항|지원자격|지원요건|담당업무|주요업무|근무조건|전형절차|접수기간 및 방법')
            
            matches = regex.finditer(text)
            # chk = re.search(r'지원자격',text)
            # if chk:
            #     start = chk.start()+1
            #     end = chk.end()-1
            #     except_text = text[start:end]
            #     logging.info(f"check except text") 
            for match in matches:
                key = match.group()
                logging.info(f"Searching  {key}-Data")
                value = text[match.end():]
                next_match = regex.search(value)
                if next_match:
                    value = value[:next_match.start()]
                # if(key=='자격요건' and chk):
                #     value = value+" "+except_text
                
                # 추가적인 전처리     
                value = value.strip()
                value = re.sub(r'\s', ' ', value)
                # except_list = ['자격요건,지원자격']

                if value:
                    if(key == "접수기간 및 방법"):
                        key = "접수기간_및_방법"
                    elif(key == "주요업무"):
                        key = "담당업무"

                    
                    item[key] = value
            # if item:
            #     item_lenght = [len(x) for x in item.values()]
            #     check_empty_item = reduce(lambda x, y: x & y, item_lenght)
            #     if(check_empty_item == 0):
            #         return 

            return item

        else:
            print("Crawling Faild")
            print(cp_text)


    