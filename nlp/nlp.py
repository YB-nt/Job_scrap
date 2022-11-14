from konlpy.tag import Okt
import pandas as pd
import psycopg2
from collections import Counter


_host ="arjuna.db.elephantsql.com"
_database="xbegavim"
_user ="xbegavim"
_password ="m7_4leTxqwHlcCKKYhhuL3SXO2dHUmo5"
conn = psycopg2.connect(
        host=_host,
        database=_database,
        user=_user,
        password=_password)
cur = conn.cursor()

temp_main =[]
temp_require =[]
temp_common=[]
temp_pt=[]

for col_name in ["job_main","require","common","pt"]:
    cur.execute(f"SELECT {col_name} FROM split_data")
    col_data = cur.fetchall()
    temp_count =[]
    temp_list = []
    for idx,data in enumerate(col_data):
        if("정보" in data[0] or "없음" in data[0]):
            continue
        if(idx==0):
            temp_list = temp_main
        elif(idx==1):
            temp_list = temp_require
        elif(idx==2):
            temp_list = temp_common
        elif(idx==3):
            temp_list = temp_pt
        


        noun = Okt().nouns(data[0])
        count = Counter(noun)
        common_list = count.most_common(10)
        temp_list.append(common_list)

    
print('='*100)
print(temp_main)
print('='*100)
print(temp_require)
print('='*100)
print(temp_common)
print('='*100)
print(temp_pt)
print('='*100)









