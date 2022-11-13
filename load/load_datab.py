import pandas as pd
import psycopg2
from psycopg2.errors import UniqueViolation
from util import data_scaling

class connect_db:
    def __init__(self,host,database,user,password):
        self.input_host = host
        self.input_database = database
        self.input_user = user
        self.input_password = password
        # print("="*150)
        self.conn = psycopg2.connect(
            host=self.input_host,
            database=self.input_database,
            user=self.input_user,
            password=self.input_password)
        self.cur = self.conn.cursor()
    def c_table_data_split(self):
        self.cur.execute("""CREATE TABLE split_data(
                                    idx int PRIMARY KEY,
                                    lnk VARCHAR(500) not null,
                                    job_main VARCHAR(10000) not null,
                                    require VARCHAR(10000) not null,
                                    common VARCHAR(10000) not null,
                                    pt VARCHAR(8000)
                                );
                            """)
        self.conn.commit()


    def c_table_saramin(self):
        self.cur.execute("""CREATE TABLE saramin(
                                        idx int PRIMARY KEY,
                                        job_name varchar(50) NOT NULL,
                                        job_section varchar(16384) NOT NULL,
                                        link varchar(500) NOT NULL,
                                        cn_name varchar(50) NOT NULL
                                    );
                                """)
        self.conn.commit()

    def c_table_wanted(self):
        self.cur.execute("""CREATE TABLE wanted(
                                        idx int PRIMARY KEY,
                                        job_name varchar(50) NOT NULL,
                                        job_section varchar(16384) NOT NULL,
                                        link varchar(500) NOT NULL,
                                        cn_name varchar(50) NOT NULL
                                    );
                                """)
        self.conn.commit()

    def c_table_total_data(self):
        self.cur.execute("""CREATE TABLE total_data(
                                    idx int PRIMARY KEY,
                                    job_name varchar(50) NOT NULL,
                                    job_section varchar(16384) NOT NULL,
                                    link varchar(500) NOT NULL,
                                    cn_name varchar(50) NOT NULL
                                );
                            """)
        self.conn.commit()

    def create_site_table(self,opt):
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
                    print('--URL OVERLAB--')
                    continue
      
        
        self.conn.commit()
        self.display_table_value(table_name=table_name)

    def split_data_load(self,df):
        for idx in range(0,df.shape[0]):
            split_data =[]
            data = df['job_section'].loc[idx]
            split_data = data_scaling.text_split(data)
            split_data.insert(0,idx)
            try:    
                self.cur.execute(f"INSERT INTO split_data VALUES {tuple(split_data)}")
            except:
                try:
                    self.cur.execute("rollback")
                    self.cur.execute(f"INSERT INTO  VALUES {tuple(split_data)}")
                except UniqueViolation:
                    print('--URL OVERLAB--')
                    continue

    def exit_db(self):
        self.cur.close()
        self.conn.close()



    
        