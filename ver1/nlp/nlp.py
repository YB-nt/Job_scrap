from konlpy.tag import Okt
import psycopg2
from collections import Counter
import re
import nltk
from pprint import pprint

nltk.download('all')
from konlpy.tag import Twitter; t = Twitter()


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

# count =0
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


        _data = data[0]
        counter = Counter(t.morphs(_data))
        eng_data = [i for i in counter.most_common() if i[0].encode().isalpha()]
        for i in eng_data:
            if(len(i[0])>10):
                eng_data.remove(i)
                counter.update(re.findall('[A-Z][^A-Z]*',i[0]))
        ko_data = Counter(Okt().nouns(_data)).most_common(len(eng_data))
        temp_list.extend(eng_data)        
        temp_list.extend(ko_data)        

sorted_main = sorted(list(set(d for d in temp_main if len(d[0])>1)),key=lambda x :-x[-1])
sorted_require = sorted(list(set(d for d in temp_require if len(d[0])>1)),key=lambda x :-x[-1])
sorted_common = sorted(list(set(d for d in temp_common if len(d[0])>1)),key=lambda x :-x[-1])
sorted_pt = sorted(list(set(d for d in temp_pt if len(d[0])>1)),key=lambda x :-x[-1])


temp_main.sort(key=lambda x:-x[1])
temp_require.sort(key=lambda x:-x[1])
temp_common.sort(key=lambda x:-x[1])
temp_pt.sort(key=lambda x:-x[1])


temp_main = [t for t in temp_main if t[1]!= 1]
temp_require = [t for t in temp_require if t[1]!= 1]
temp_common = [t for t in temp_common if t[1]!= 1]
temp_pt = [t for t in temp_pt if t[1]!= 1]


# tuple removing duplication
duplication_d = set()
_temp_pt = []
for a,b in temp_pt:
    if not a in duplication_d:
        duplication_d.add(a)
        _temp_pt.append((a,b))

temp_pt = _temp_pt

print('='*100)
print(temp_main)
print('='*100)
print(temp_require)
print('='*100)
print(temp_common)
print('='*100)
print(temp_pt)
print('='*100)







>>>>>>> cd2111053b0607e37fa208f03ca970fff1b4a317


print("="*100)
print("job_main : ")
pprint(sorted_main)
print("="*100)
print("common_require : ")
pprint(sorted_common)
print("="*100)
print("require : ")
pprint(sorted_require)
print("="*100)
print("pt : ")
pprint(sorted_pt)
print("="*100)