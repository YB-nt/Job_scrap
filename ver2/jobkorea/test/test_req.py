import requests 
from pprint import pprint
from bs4 import BeautifulSoup as soup 
import chardet

class Req_jobkorea:
    def __init__(self):
        self.urls =[
            "https://www.jobkorea.co.kr/Recruit/GI_Read/40933613"
        ]
        self.headers = ""
        for url in self.urls:
            self.response = requests.get(url,headers=self.headers)            
    def parse(self):
        if(self.response.status_code==200):
            page = soup(self.response.text,'html.parser')
            temp =[]

            for i in page.text.encode("utf-8"):
                # print(i)
                try:
                    temp.append(chr(i))
                except TypeError:
                    temp.append(i)

            
            for i in range(0,len(temp)-1):
                # try:
                temp[i] = temp[i].encode('utf-8')
                if(type(temp[i]) is bytes):
                    # 나온 인코딩 방식별로 분류 해주기 
                    if(chardet.detect(temp[i])['encoding']=="ascii"):
                    # elif("Windows-1252"):
                    # elif("ISO-8859-1"):
                    # elif("utf-8"):
                    # elif('TIS-620'):
                else:
                    print("not bytes")
                    print(temp[i])
                    print("="*20)
                
            # for word in temp:
            #     





jobkorea = Req_jobkorea()
print(jobkorea.parse())



