import requests as req
from bs4 import BeautifulSoup as soup 
import re
import pandas as pd


class sarmain:
    def __init__(self,keyword):
        self.keyword = keyword
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Whale/3.16.138.27 Safari/537.36'}
        self.search_base_url = "https://www.saramin.co.kr/zf_user/search?searchword="
        self.add_url = self.search_base_url + self.keyword
        self.base_url = "https://www.saramin.co.kr"
        # keyword = input("input keyword: ")
        # keyword='데이터 엔지니어'

# test
    def make_url_list(self):
        for page_num  in range(1,6):
            update_url=f"{self.add_url}&recruitPage={page_num}"
            resp = req.get(update_url,headers=self.headers)
            url_list = []
            job_tit =[]
            cname=[]
            if(resp.status_code==200):
                page_source = soup(resp.text,"html.parser")
                contents = page_source.find("div",class_='content')
                # h2 class : job_tit
                company_name = contents.find_all("strong",class_='corp_name')
                job_title = contents.find_all("h2",class_="job_tit")

                for lnk,c in zip(job_title,company_name):
                    url_list.append(lnk.find('a',href=True)['href'])
                    job_tit.append(lnk)
                    cname.append(c)            
            else:
                print(resp.status_code)
        return url_list,job_title,company_name

    def make_df(self,dic):
        print('-'*100)
        print("Make DataFrame")
        print('-'*100)
        df = pd.DataFrame(dic)
        return df
    
    def scraper(self):
        url_list,job_title,company_name = self.make_url_list()
        total_url = [self.base_url+url for url in url_list]
        detail_page =[]
        for lnk in total_url:   
            detail_content_num = re.search('rec_idx=(.+?)$',lnk).group(1)
            detail_page.append(f'https://www.saramin.co.kr/zf_user/jobs/relay/view-detail?rec_idx={detail_content_num}&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content=')

        # test_page = detail_page[:10]
        access_page = []
        except_page = []
        access_link = []
        access_cname=[]
        access_title=[]
        # print(len(detail_page))
        for lnk,jt,cn in zip(detail_page,job_title,company_name):
            resp = req.get(lnk,headers=self.headers)
            if(resp.status_code==200):
                page_source = soup(resp.text,"html.parser")

                contents = page_source.find('div',class_='wrap_tbl_template')
                if(contents!=None):
                    page_text = contents.text
                    access_page.append(page_text)
                    access_link.append(lnk)
                else:
                    contents=page_source.find('div',class_='user_content')
                    if(contents!=None):
                        page_text=contents.text
                        access_page.append(page_text)
                        access_link.append(lnk)
                    else:
                        except_page.append(lnk)
                access_cname.append(cn)
                access_title.append(jt)
            else:
                print(resp.status_code)

        return access_link,access_page,access_cname,access_title

    def data_load(self):
        dic_job_scrap = {"job_name":"","job_section":"","link":"","cn_name":""}

        temp_list_lnk,temp_list_section,temp_list_cname,temp_list_j_name=self.scraper()

        dic_job_scrap["job_name"]= temp_list_j_name
        dic_job_scrap["job_section"]=temp_list_section
        dic_job_scrap['link'] = temp_list_lnk
        dic_job_scrap['cn_name'] = temp_list_cname

        df = self.make_df(dic_job_scrap)
        return df



