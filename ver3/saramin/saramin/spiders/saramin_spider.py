import scrapy
from scrapy.http import Request
from saramin.items import SaraminItem_info
from saramin.pipelines import SaraminPipeline
import re,copy
# from pprint import pprint
from datetime import datetime
from functools import reduce
import logging


class JobSpider(scrapy.Spider):
    name = "saramin"
    search_keyword =["데이터 엔지니어",'데이터엔지니어','data engineer','MLOps']
    start_urls = [f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=recently&searchword={keyword}" for keyword in search_keyword]
    
    

    def __init__(self):
        self.extract_num =""

    def parse(self, response):
        a_job_tits = response.xpath('//h2[@class="job_tit"]')
        for a_job_tit in a_job_tits:
            job_num = a_job_tit.xpath('./a/@href').get()
            self.extract_num = re.findall(r'(?<=rec_idx=)[0-9]+',job_num)[0]
            summary_link = f'https://www.saramin.co.kr/zf_user/jobs/relay/view-detail?rec_idx={self.extract_num}&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content='
            yield Request(url=summary_link,callback=self.detail_parse)
            

    def detail_parse(self, response):
        # logging.info(f"Searching URL ::{response.url}")
        text = response.xpath("//table[@class='cont_recruit_template']//text()").getall()
        if(len(text)==0):
            text=response.xpath("/html/body/div/div/div[3]/div[2]//text()").getall()
        if(len(text)==0):
            text =response.xpath("(//div[@class='user_content']//dl)[2]//text()").getall()

        if(len(text)!=0):
            if(type(text)==list):
                text = ', '.join(text)
            

        yield self.preprocess(text,url=response.url)
        
    def preprocess(self, text,url):
        
        cp_text = copy.deepcopy(text)
        
        if cp_text is not None:
            text = str(cp_text)
            text = re.sub(r'[^\w\s-]', '', text)
            regex = re.compile(r'자격요건|우대사항|지원자격|지원요건|담당업무|주요업무|근무조건|전형절차|접수기간 및 방법')
            except_list  = ['지원자격','지원요건','자격요건','temp']
            matches = regex.finditer(text)
            id = re.findall(r'(?<=rec_idx=)[0-9]+',url)[0]
            temp_dic = {}
            temp_dic['id'] = id
            for match in matches:
                key = match.group()

                # 현재 어떠한 데이터를 저장하고있는지 시각화해서 보기 위한 로그 
                # logging.info(f"Searching  {key}-Data")

                value = text[match.end():]
                next_match = regex.search(value)

                if next_match:
                    value = value[:next_match.start()]
                value = value.strip()
                value = re.sub(r'\s', ' ', value)

                if value:
                    if(key == "접수기간 및 방법"):
                        key = "접수기간_및_방법"
                    elif(key == "주요업무"):
                        key = "담당업무"
    
                    temp_dic[key] = value
            
            check_item = [x for x in temp_dic.keys() if x in except_list]
            if(len(check_item)>1):
                for i,v in enumerate(check_item):    
                    if(v=='자격요건'):
                        continue
                    temp_dic['자격요건']+=str(" "+temp_dic[v])
                    del(temp_dic[check_item[i]])
            elif(len(check_item)==1):
                if(check_item[0]!='자격요건'):
                    temp_value = temp_dic[check_item[0]]
                    del(temp_dic[check_item[0]])
                    temp_dic['자격요건'] = temp_value
            else:
                pass

            if(len(temp_dic.keys())>1):
                return self.return_item(temp_dic)
        else:
            print("PASS")
            # logging.debug(f"Failed Load Data:{cp_text}")


    def return_item(self,temp_dict):
        item = SaraminItem_info()
        for k in temp_dict.keys():
            item[k] = temp_dict[k]
        return item


        