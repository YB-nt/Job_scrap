import pandas as pd
import psycopg2

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

    def c_table_saramin(self):
        try:
            self.cur.execute("""CREATE TABLE saramin(
                                        job_name varchar(100) PRIMARY KEY,
                                        job_section varchar(500) NOT NULL,
                                        link varchar(150) NOT NULL,
                                        cn_name varchar(30) NOT NULL
                                    );
                                """)
            self.conn.commit()
        except:
            pass

    def c_table_wanted(self):
        try:
            self.cur.execute("""CREATE TABLE wanted(
                                        job_name varchar(100) PRIMARY KEY,
                                        job_section varchar(500) NOT NULL,
                                        link varchar(150) NOT NULL,
                                        cn_name varchar(30) NOT NULL
                                    );
                                """)
            self.conn.commit()
        except:
            pass

    def c_table_total_data(self):
        try:
            self.cur.execute("""CREATE TABLE total_data(
                                        job_name varchar(100) PRIMARY KEY,
                                        job_section varchar(500) NOT NULL,
                                        link varchar(150) NOT NULL,
                                        cn_name varchar(30) NOT NULL
                                    );
                                """)
            self.conn.commit()
        except:
            pass

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
        self.cur.execute("SELECT tablename  FROM pg_catalog.pg_tables where schemaname = 'public';")
        table_check = self.cur.fetchall()
        # print(table_check,type(table_check))
        if(opt==-1):
            pass

        if(opt==0):
            if("saramin" in table_check):
                pass
            else:
                self.c_table_saramin()

        if(opt==1):
            if("wanted" in table_check):
                pass
            else:
                self.c_table_wanted()

        if(opt==2):
            if("saramin" in table_check):
                if("wanted" in table_check):
                    pass
                else:
                    self.c_table_wanted()
            else:
                self.c_table_saramin()
                if("wanted" in table_check):
                    pass
                else:
                    self.c_table_wanted()

        if(opt==3):
            if("total_data" in table_check):
                self.c_table_total_data()
            else:
                pass

        if(opt==4):
            if("saramin" in table_check):
                if("wanted" in table_check):
                    if("total_data" in table_check):
                        pass
                    else:
                        self.c_table_total_data()
                else:
                    self.c_table_wanted()
                    if("total_data" in table_check):
                        pass
                    else:
                        self.c_table_total_data()
            else:
                self.c_table_saramin()
                if("wanted" in table_check):
                    pass
                else:
                    self.c_table_wanted()
                    if("total_data" in table_check):
                        pass
                    else:
                        self.c_table_total_data()

 
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

        print("Wanted")
        print("#"*100)
        print(pd.read_sql_table('Total_Table',self.conn))
        print("#"*100)

    def merge_df(self,df1,df2):
        df = pd.concat([df1,df2],ignore_index=True)
        return df

    def load_data(self,df,table_name):
        for idx in range(0,df.shape[0]+1):    
            self.cur.execute(f"INSERT INTO {table_name} VALUES {tuple(v for v in df.loc[idx])}")
            self.conn.commit()
        self.display_table_value()



    
        