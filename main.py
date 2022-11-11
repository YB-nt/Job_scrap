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
        sarmain_df,wanted_df = self.extract()
        for df in [sarmain_df,wanted_df]:
            for col in df.columns:
                if(col=='job_section'):
                    data_scaling.col_preprocessing(df,str(col))
                elif(col=='link'):
                    continue
                data_scaling.col_preprocessing2(df,str(col))

        return sarmain_df,wanted_df
        
    def load(self):

        load_data = load_datab.connect_db(self.host,self.database,self.user,self.password) 
        saramin,wanted = self.transfrom()
        
        load_data.create_site_table(self.cdb)
        total = load_data.merge_df(saramin,wanted)
        
        if(self.cdb==-1):
            load_data.load_data(wanted, table_name = "saramin") 
            load_data.load_data(wanted, table_name = "wanted")
            load_data.load_data(total, table_name = "total_data")  
        if(self.cdb==0):
            load_data.load_data(saramin, table_name = "saramin")
        elif(self.cdb==1):
            load_data.load_data(wanted, table_name = "wanted")
        elif(self.cdb==2):
            load_data.load_data(saramin, table_name = "saramin")
            load_data.load_data(wanted, table_name = "wanted")
        elif(self.cdb==3):
            load_data.load_data(total, table_name = "total_data") 
        elif(self.cdb==4):
            load_data.load_data(saramin, table_name = "saramin") 
            load_data.load_data(wanted, table_name = "wanted")
            load_data.load_data(total, table_name = "total_data") 

        load_data.exit_db()
        return saramin,wanted

    def job_scraping(self):
        saramin,wanted = self.load()

        saramin.to_csv('./csv/saramin.csv')
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




