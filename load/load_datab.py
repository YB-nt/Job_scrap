import pandas as pd
import psycopg2
from psycopg2.errors import UniqueViolation
from util import data_scaling

class connect_db:
    def __init__(self,keyword,must_keyword,host,database,user,password,testopt):
        self.must_keyword = must_keyword
        self.keyword = keyword
        self.input_host = host
        self.input_database = database
        self.input_user = user
        self.input_password = password
        self.testopt = testopt
        # print("="*150)
        self.conn = psycopg2.connect(
            host=self.input_host,
            database=self.input_database,
            user=self.input_user,
            password=self.input_password)
        self.cur = self.conn.cursor()
    def c_table_data_split(self):
        try:
            self.cur.execute("""CREATE TABLE split_data(
                                        idx int PRIMARY KEY,
                                        lnk VARCHAR(500) not null,
                                        job_main VARCHAR(16384),
                                        require VARCHAR(16384),
                                        common VARCHAR(16384),
                                        pt VARCHAR(8000)
                                    );
                                """)
            self.conn.commit()
        except:
            pass

    def c_table_saramin(self):
        try:
            self.cur.execute("""CREATE TABLE saramin(
                                            idx int PRIMARY KEY,
                                            job_name varchar(500) NOT NULL,
                                            job_section varchar(16384) NOT NULL,
                                            link varchar(500) NOT NULL,
                                            cn_name varchar(50) NOT NULL
                                        );
                                    """)
            self.conn.commit()
        except:
            pass
    def c_table_wanted(self):
        try:
            self.cur.execute("""CREATE TABLE wanted(
                                            idx int PRIMARY KEY,
                                            job_name varchar(500) NOT NULL,
                                            job_section varchar(16384) NOT NULL,
                                            link varchar(500) NOT NULL,
                                            cn_name varchar(50) NOT NULL
                                        );
                                    """)
            self.conn.commit()
        except:
            pass
    def c_table_total_data(self):
        try:
            self.cur.execute("""CREATE TABLE total_data(
                                        idx int PRIMARY KEY,
                                        job_name varchar(500) NOT NULL,
                                        job_section varchar(16384) NOT NULL,
                                        link varchar(500) NOT NULL,
                                        cn_name varchar(50) NOT NULL
                                    );
                                """)
            self.conn.commit()
        except:
            pass
    def create_site_table(self,opt):
        self.test_init()
        """
                            Create Database\n
                            0: saramin\n
                            1: wanted\n
                            2: saramin,wanted\n
                            3: total_data\n
                            4: all\n
                            -1: None
        """
        print("Create_Table!")
        print("##CREATE TABLE##")
        self.cur.execute("SELECT tablename  FROM pg_catalog.pg_tables where schemaname = 'public';")
        table_check = self.cur.fetchall()
        self.conn.commit()
        # print(table_check,type(table_check))
        if(opt==-1):
            print("opt1 pass")
        else:
            self.c_table_data_split()

        if(opt==0):
            if("saramin" not in table_check):
                self.c_table_saramin()
            else:
                print("saramin check")

        elif(opt==1):
            if("wanted" not in table_check):
                self.c_table_wanted()
            else:
                print("wanted check")

        elif(opt==2):
            if("saramin" not in table_check):
                if("wanted" not in table_check):
                    self.c_table_wanted()
                else:
                    print("wanted check")
            else:
                self.c_table_saramin()
                if("wanted" not in table_check):
                    self.c_table_wanted()
                else:
                    print("wanted check")

        elif(opt==3):
            if("total_data" not in table_check):
                self.c_table_total_data()
            else:
                print("total check")

        elif(opt==4):
            if("saramin" not in table_check):
                if("wanted" not in table_check):
                    if("total_data" not in table_check):
                        self.c_table_total_data()
                        self.c_table_wanted()
                        self.c_table_saramin()
                    else:
                        self.c_table_wanted()
                        self.c_table_saramin()
                else:
                    if("total_data" not in table_check):
                        self.c_table_total_data()
                        self.c_table_saramin()
                    else:
                        print("total check")
            else:
                if("wanted" not in table_check):
                    self.c_table_wanted()
                    if("total_data" not in table_check):
                        self.c_table_total_data()
                    else:
                        print("total check")
                else:
                    if("total_data" not in table_check):
                        self.c_table_total_data()
                    else:
                        print("total check")

    def test_init(self):
        if(self.testopt is True):
            print("="*30)
            print("TESTING!! ---- drop table")
            print("="*30)
            self.cur.execute("SELECT tablename  FROM pg_catalog.pg_tables where schemaname = 'public';")
            table_check = self.cur.fetchall()
            print(table_check)
            for i in table_check:
                try:
                    self.cur.execute(f"drop table {i[0]}")
                except:
                    try:
                        self.cur.execute("rollback")
                        self.cur.execute(f"drop table {i[0]}")
                    except:
                        pass
            self.conn.commit()
                    

    def display_table_value(self,table_name):
        print("="*100)
        print(">> Complte Data load")        
        print("="*100)
        print(f'{table_name}')
        print("="*100)
        self.cur.execute(f"SELECT * FROM {table_name}")
        for i in self.cur.fetchall()[:3]:
            print(i)
        self.conn.commit()

    def merge_df(self,df1,df2):
        df = pd.concat([df1,df2],ignore_index=True)
        return df

    def load_data(self,df,table_name):
        for idx in range(0,df.shape[0]):
            value = [v for v in df.loc[idx]]
            value.insert(0,idx)
            try:    
                self.cur.execute(f"INSERT INTO {table_name} VALUES {tuple(value)}")
            except:
                try:
                    self.cur.execute("rollback")
                    self.cur.execute(f"INSERT INTO {table_name} VALUES {tuple(value)}")
                except UniqueViolation:
                    print('--OVERLAB--')
                    continue
                
        self.conn.commit()
        self.display_table_value(table_name=table_name)

    def split_data_load(self,df):
        print('='*100)
        for idx in range(0,df.shape[0]):
            job_main=''
            require=''
            common_require=''
            pref=''

            data = df['job_section'].loc[idx]
            lnk = df['link'].loc[idx]

            if("saramin" in lnk ):
                if(any(k in data for k in self.must_keyword)):
                    pass
                else:
                    continue
            
            

            job_main,require,common_require,pref = data_scaling.text_split(data,self.keyword)
            if(len(job_main)>8500 or \
                len(require)>8500 or \
                len(common_require)>8500 or \
                len(pref)>8500):
                continue
            

            value =[idx,lnk,job_main,require,common_require,pref]
            # print(tuple(value))                        
            try:    
                self.cur.execute(f"INSERT INTO split_data VALUES {tuple(value)}")
            except:
                try:
                    self.cur.execute("rollback;")
                    self.cur.execute(f"INSERT INTO split_data VALUES {tuple(value)}")
                except Exception as e:
                    print(e)
                    continue

    def exit_db(self):
        self.cur.close()
        self.conn.close()



    
        