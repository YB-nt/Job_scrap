# # # # # # # # import re


# # # # # # # # # # text = """        우대사항데이터사이언티스트 0명담당업무ㆍ[담당업무]ㆍ쇼핑플랫폼의 Front-end AI 시스템 개발 (Optimization,CF,FM)ㆍ가격
# # # # # # # # # # 비교플랫폼의 Back-end AI 시스템 개발 (NLP,CNN,RNN)[자격요건]ㆍ경력 : 신입 ~ 3년이하ㆍ원활한 커뮤니케이션 능력으로 차분히 논 
# # # # # # # # # # 리를 전개하실 수 있는 분ㆍMachine Learning관련 학위 혹은 관련된 프로젝트 경험이 있으신 분ㆍ수작업을 자동화하고 업무를 효율화
# # # # # # # # # #  하면서 끊임 없는 성능개선에 즐거움을 느끼시는 분ㆍ데이터를 가공/시각화하고 이를 분석하여 인사이트를 얻고 설득하는 것에 즐거
# # # # # # # # # # 움을 느끼시는 분[우대사항]ㆍ R,Python,C++ 중 한가지 언어를 능숙하게 다루시는 분ㆍ Keras(Tensorflow) 기반의 NLP분야의 Deep Learning 경험이 있으신 분ㆍ Kaggle 등 머신러닝 대회 참가 경험이 있으신 분
# # # # # # # # # # """
# # # # # # # # # # string ='''데이터 엔지니어 0명담당업무ㆍ■ 수행업무 LG계열사 DW관련 SI/SM 사업 수행Bigata / DataLake 데이터 파이프라인 구축DW/DataMart 설계,개발■ 지원요건 [ 필수 - BI/DW 데이터 설계 or ETL ]   - DW/DM 분석/설계 경험 또는
# # # # # # # # # #     - ETL Tool ( Informatica, Datastage, Terasteam 등 ) 또는 SQL, PL/SQL 활용한 DW / BigData  정보계 프로젝트      데이터 Migration / ETL 경험 보유[ 우대 - BI/DW 관련 on-premise or 클라우드 솔루션 구축 경험 ]  - OLAP ( MSTR, BI-MATRIX 등 ),   BI ( Tableau, Power BI, Spotfire등 ) 개발/운영 경험 보유  - Spark, Python 기반 데이터 파이프라인 구축 경험   - AWS / GCP / AZURE 등 클라우드 기반 빅데이터 구축 경험 ( S3, RedShift, GCS, Big Query )   - Hadoop, Vertica, Sybase 등 다양한 DB기반 구축 경험 
# # # # # # # # # #             ㆍ기타 필수 사항
# # # # # # # # # #         우대사항'''




# # # # # # # # # # p1=re.compile("우대사항")
# # # # # # # # # # p2=re.compile("담당업무")
# # # # # # # # # # p3=re.compile("자격요건")
# # # # # # # # # # # p4=re.compile("우대사항")
# # # # # # # # # # # p= re.compile('[\r\n\v]')
# # # # # # # # # # result1 = p1.split(string) #mid
# # # # # # # # # # result2 = p2.split(max(result1,key=len))#mid
# # # # # # # # # # result3 = p3.split(max(result2,key=len))#max
# # # # # # # # # # result4 = max(result3,key=len)

# # # # # # # # # # # print("1",min(result1,key=len))
# # # # # # # # # # # print("2",min(result2,key=len))
# # # # # # # # # # # print("3",min(result3,key=len))
# # # # # # # # # # # print("4",min(result4,key=len))

# # # # # # # # # # # print("4:",max(result3,key=len))
# # # # # # # # # # print(result4)



# # # # # # # # # # # for _ in p.finditer(text):
# # # # # # # # # # #     print()
# # # # # # # # # # #     print(text[_.start():])






# # # # # # # # # common = """
# # # # # # # # #  ㆍ학력 : 대졸 이상 (4년)S/W F/W 엔지니어S/W팀 0명담당업무ㆍ임베디드 시스템 S/W, F/W 개발 ㆍ전장/제어시스템 S/W, F/W 개발ㆍTCP/IP기반 통신 시스템 S/W개발ㆍMultimedia(Audio/Video) 시스템 S/W개발지원자격
# # # # # # # # # ㆍ경력 : 무관
# # # # # # # # # """

# # # # # # # # # print(")" in common[:20])
# # # # # # # # # print(len("ㆍ학력 : 대졸 이상 (4년)"))
# # # # # # # # # print(common[len("ㆍ학력 : 대졸 이상 (4년)")+1])



# # # # # # # # # string = """<h6 style="max-width: calc(100% - 69px);"><a href="/company/5603" class="" aria-label="" data-attribute-id="company__click" data-company-id="5603" data-company-name="두잉랩">두잉랩</a></h6>
# # # # # # # # # """

# # # # # # # # # p = r'max\-width\: calc\(100% \- [0-9]*px\);'

# # # # # # # # # test = re.findall(p,string)[0]

# # # # # # # # # print(test)



# # # # # # # # import class_selenium
# # # # # # # # import class_saramin

# # # # # # # # # wanted_data = class_selenium.wanted('데이터엔지니어')
# # # # # # # # # print(wanted_data.job_detail())

# # # # # # # # saramin_data = class_saramin.sarmain('데이터 엔지니어')
# # # # # # # # print(saramin_data.data_load())



# # # # # # # import psycopg2


# # # # # # # conn = psycopg2.connect(
# # # # # # #             host="arjuna.db.elephantsql.com",
# # # # # # #             database="xbegavim",
# # # # # # #             user="xbegavim",
# # # # # # #             password="m7_4leTxqwHlcCKKYhhuL3SXO2dHUmo5")
# # # # # # # cur = conn.cursor()
# # # # # # # try:

# # # # # # #     cur.execute("""CREATE TABLE test(
# # # # # # #                     job_name VARCHAR(100) PRIMARY KEY,
# # # # # # #                     job_section VARCHAR(500) NOT NULL,
# # # # # # #                     link VARCHAR(150) NOT NULL,
# # # # # # #                     cn_name VARCHAR(30) NOT NULL
# # # # # # #                 );""")
                
# # # # # # # except Exception as e:
# # # # # # #     print("#ERROR#",e)
    




# # # # # # # conn.commit()
# # # # # # # # cur.execute("SELECT * FROM pg_catelaog.pg_tables where schemaname='public'")



# # # # # # # # cur.execute("insert into test values('asdf','asdf','asdwwf','asdfdd')")
# # # # # # # # cur.execute("SELECT job_name FROM test")
# # # # # # # # result = cur.fetchone()
# # # # # # # # conn.commit()
# # # # # # # # print(result)
# # # # # # # # print("type:",type(result))
# # # # # # # # print(type(result[0]))
    
# # # # # # import re
# # # # # # string ="\\n\\b\b\대졸 이상 (4년)S/W F/W 엔지니어S/W팀 0명담당업무\\n\n\\\b\n"



# # # # # # # string = re.sub('\s|\\.|\n|&(^[가-힣]*|[a-z]*)','',string)
# # # # # # # print(string)
# # # # # # string = re.sub('\s|(\\.^[가-힣]*|[a-z]+)|\n','',string).replace("\\",'')
# # # # # # print(string)




# # # # # import pandas as pd 


# # # # # df = pd.DataFrame({'t1':[1,2,3,4,5],'t2':[5,4,32,1,0]})
# # # # # df_m = pd.DataFrame({'t1':[12,22,32,42,52],'t2':[53,43,323,133,303]}) 

# # # # # df = pd.concat([df,df_m],ignore_index=True)
# # # # # print(df)




# # # # # import sys,os
# # # # # sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# # # # # from load import load_datab 

# # # # # _host ="arjuna.db.elephantsql.com"
# # # # # _database="xbegavim"
# # # # # _user ="xbegavim"
# # # # # _password ="m7_4leTxqwHlcCKKYhhuL3SXO2dHUmo5"
# # # # # l = load_datab.connect_db(_host,_database,_user,_password)
# # # # # l.create_site_table(4)


# # # # import pandas as pd

# # # # df = pd.DataFrame({'t1':[1,2,3,4,5],'t2':[5,4,32,1,0]})

# # # # row = tuple(x for x in df.loc[1])
# # # # print(row)


# # # import re 

# # # string ="""담당업무
# # # ㆍ빅데이터분석 /  스마트EMS개발 / 스마트PMS개발
# # # ㆍ데이터분석, 인공지능 모델링/알고리즘
# # # ㆍ머신러닝/딥러닝 데이터 파이프라인 설계 및 구축
# # # ㆍPMS(예지보존), EMS(에너지관리) 데이터분석 및 관리시스템 개발
# # # ㆍPMS, EMS시스템의 고객사 시스템과 연계구축 방안 정의

# # # 자격조건
# # # ㆍ학력 : 초대졸이상 (졸업예정자 가능)
# # # ㆍ경력 : 경력무관

# # # 우대사항
# # # ㆍ유관업무 경험자(인턴·알바)
# # # ㆍ관련 자격증 보유자
# # # ㆍ고장진단 및 예지보전 데이터 분석 업무에 대한 경험 우대
# # # ㆍ데이터 기반의 에너지 최적화 및 최적제어 업무에 대한 경험 우대함께하기 위한 방법접수기간 : 2022년 11월 07일 (월)12시 00분 ~ 2022년 12월 07일 (수) 23시 59분접수방법 : 사람인 입사지원이력서양식 : 사람인 이력서 양식함께하기 위 
# # # 한 여정서류전형1차면접최종합격"""
# # # t1 = re.sub('[^\uAC00-\uD7A30-9a-zA-Z\s]','',string)
# # # t2 = re.sub('\n','',t1)
# # # print(t2)

# # l = [1123,12,134,1230]
# # print(l)
# # l.insert(0,3)


# # print(l)


# check1 = "https://www.saramin.co.kr/zf_user/jobs/relay/view-detailrec_idx=44467294&location=ts&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0+%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4&searchType=search&paid_fl=n&search_uuid=6b91adbc-e5be-4541-84b5-213353606b15&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content="

#          "https://www.saramin.co.kr/zf_user/jobs/relay/view-detail?rec_idx=44467294&location=ts&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0+%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4&searchType=search&paid_fl=n&search_uuid=8ee2c72d-8a53-4fe2-a301-b4339be0fcdf&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content= "
# check2 = "https://www.saramin.co.kr/zf_user/jobs/relay/view-detail?rec_idx=44467295&location=ts&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0+%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4&searchType=search&paid_fl=n&search_uuid=6b91adbc-e5be-4541-84b5-213353606b15&rec_seq=0&t_category=relay_view&t_content=view_detail&t_ref=&t_ref_content="

# for i in zip(check1,check2):
#     if(i[0]==i[1]):
#         pass
#     else:
#         print("i:",i[0])
#         print("j",i[1])


Input = [(12.121, 'Geeksforgeeks is best'), 
         (19212.22, 'India is best'), 
         (12.121, 'Cyware is best.'),
         (923232.2323, 'Jiit is best')]
  
# using set
visited = set()
  
# Output list initialization
Output = []
  
# Iteration
for a, b in Input:
    if not a in visited:
        visited.add(a)
        Output.append((a, b))
  
# Printing
print("Initial list of tuple is \n", Input)
print("List of tuple after removing duplicates:\n ", Output)