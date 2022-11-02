import psycopg2

class connect_db:
    def __init__(self):
        self.input_host = input("서버 호스트 주소: ")
        self.input_database = input("데이터베이스 이름: ")
        self.input_user = input("유저이름: ")
        self.input_password = input("유저 비밀번호: ")
        print()
        self.conn = psycopg2.connect(
            host=self.input_host,
            database=self.input_database,
            user=self.input_user,
            password=self.input_password)
        self.cur = self.conn.cursor()
        
    def create_site_table(self):
        self.cur.execute("""CREATE TABLE saramin(
                        
                        );
                    """)
        self.cur.commit()
        self.cur.execute("""CREATE TABLE wanted(
        
                        );
                    """)
        self.cur.commit()
        

    def load_data(self):
        #DataFrame data load part 
        self.cur.execute("""(
        
                        );
                    """)
        self.cur.commit()

    
        