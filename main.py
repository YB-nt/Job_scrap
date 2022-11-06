from ast import keyword
from job_scrap import class_saramin,class_wanted
from load import load_datab
from util import data_scaling
import pandas as pd


class Job_scraping:
    def __init__(self,keyword,cdb,host,database,user,password):
       self.keyword = keyword
       self.cdb = cdb
       self.host = host
       self.database = database
       self.user = user 
       self.password = password

    def extract(self):

        sarmain = class_saramin.sarmain(self.keyword)
        saramin_df = sarmain.data_load() 
        wanted = class_wanted.wanted(self.keyword)
        wanted_df = wanted.job_detail()
        return saramin_df,wanted_df

    def transfrom(self):

        temp_section = []
    
        sarmain_df,wanted_df = self.extract()

        # saramin_df preprossesing
        for data in sarmain_df['job_section']:
            pre_data = data_scaling.text_preprocessing(data)
            structed_data = data_scaling.text_split(pre_data)
            temp_section.append(structed_data)
        sarmain_df['job_section'] = temp_section
        
        # wanted_df preprossesing
        temp_section = []
        for data in wanted_df['job_section']:
            pre_data = data_scaling.text_preprocessing(data)
            structed_data = data_scaling.text_split(pre_data)
            temp_section.append(structed_data)
        wanted_df['job_section'] = temp_section

        return sarmain_df,wanted_df
        
    def load(self):

        load_data = load_datab.connect_db(self.host,self.database,self.user,self.password) 
        sramin,wanted = self.transfrom()
        load_data.create_site_table(self.cdb)
        load_data.load_data(sramin)
        load_data.load_data(wanted)
        return sramin,wanted

    def job_scraping(self):
        sramin,wanted = self.load()
        sramin.to_csv('./csv/saramin.csv')
        wanted.to_csv('./csv/wanted.csv')
       

if __name__=="__main__":
    _keyword = "데이터 엔지니어"
    _cdb = 4

    _host ="arjuna.db.elephantsql.com"
    _database="xbegavim"
    _user ="xbegavim"
    _password ="m7_4leTxqwHlcCKKYhhuL3SXO2dHUmo5"

    scrap = Job_scraping(keyword=_keyword,cdb=_cdb\
                ,host=_host\
                ,database=_database\
                ,user=_user\
                ,password=_password)


    scrap.job_scraping()




