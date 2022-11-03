import pandas as pd
import psycopg2

class connect_db:
    def __init__(self):
        self.input_host = input("서버 호스트 주소: ")
        self.input_database = input("데이터베이스 이름: ")
        self.input_user = input("유저이름: ")
        self.input_password = input("유저 비밀번호: ")
        print("="*150)
        self.conn = psycopg2.connect(
            host=self.input_host,
            database=self.input_database,
            user=self.input_user,
            password=self.input_password)
        self.cur = self.conn.cursor()
        
    def create_site_table(self,opt):
        """
        opt1: saramin
        opt2: wanted
        opt3: both
        opt4: total_data
        opt5: all
        """
        if(opt==0):
            self.cur.execute("""CREATE TABLE saramin(
                                    job_name TEXT(100) PARIMARY KEY,
                                    job_section TEXT(500) NOT NULL,
                                    link TEXT(150) NOT NULL,
                                    cn_name(30) NOT NULL
                                );
                            """)
            self.cur.commit()
        if(opt==1):
            self.cur.execute("""CREATE TABLE wanted(
                                    job_name TEXT(100) PARIMARY KEY,
                                    job_section TEXT(500) NOT NULL,
                                    link TEXT(150) NOT NULL,
                                    cn_name(30) NOT NULL
                                );
                            """)
            self.cur.commit()
        if(opt==2):
            try:
                self.cur.execute("""CREATE TABLE saramin(
                                    job_name TEXT(100) PARIMARY KEY,
                                    job_section TEXT(500) NOT NULL,
                                    link TEXT(150) NOT NULL,
                                    cn_name(30) NOT NULL
                                );
                            """)
                self.cur.commit()
            except Exception as e1:
                print("#ERROR#",e1)
                try:
                    self.cur.execute("""CREATE TABLE wanted(
                                    job_name TEXT(100) PARIMARY KEY,
                                    job_section TEXT(500) NOT NULL,
                                    link TEXT(150) NOT NULL,
                                    cn_name(30) NOT NULL
                                );
                            """)
                    self.cur.commit()
                except Exception as e2:
                    print("#ERROR#",e2) 
        if(opt==3):
            self.cur.execute("""CREATE TABLE total_data(
                                    job_name TEXT(100) PARIMARY KEY,
                                    job_section TEXT(500) NOT NULL,
                                    link TEXT(150) NOT NULL,
                                    cn_name(30) NOT NULL
                                );
                            """)
            self.cur.commit()
        if(opt==4):
            try:
                self.cur.execute("""CREATE TABLE saramin(
                                    job_name TEXT(100) PARIMARY KEY,
                                    job_section TEXT(500) NOT NULL,
                                    link TEXT(150) NOT NULL,
                                    cn_name(30) NOT NULL
                                );
                            """)
                self.cur.commit()
            except Exception as e1:
                print("#ERROR#",e1)
                try:
                    self.cur.execute("""CREATE TABLE wanted(
                                    job_name TEXT(100) PARIMARY KEY,
                                    job_section TEXT(500) NOT NULL,
                                    link TEXT(150) NOT NULL,
                                    cn_name(30) NOT NULL
                                );
                            """)
                except Exception as e2:
                    print("#ERROR#",e2)
                self.cur.execute("""CREATE TABLE total_data(
                                    job_name TEXT(100) PARIMARY KEY,
                                    job_section TEXT(500) NOT NULL,
                                    link TEXT(150) NOT NULL,
                                    cn_name(30) NOT NULL);""")
                self.cur.commit() 
                

                
    def display_table_value(self):
        print("="*100)
        print("Complte Data load")        
        #my_table   = pd.read_sql_table('table_name', connection)
        print("#"*100)
        print("Saramin")
        print("#"*100)
        print(pd.read_sql_table('saramin',self.conn))
        print("#"*100)
        print("Wanted")
        print("#"*100)
        print(pd.read_sql_table('wanted',self.conn))
        print("#"*100)


    def load_data(self,df):
        for idx in range(0,df.shape[0]+1):    
            self.cur.execute(f"INSERT INTO VALUES{(v for v in df.loc[idx])}")
        self.cur.commit()
        self.display_table_value()


    
        