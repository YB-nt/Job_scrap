import re

def text_preprocessing(page_text):
    # page_text = re.sub('\s|(\\.^[가-힣]*|[a-z]+)|\n','',page_text)
    r_t = re.sub('[^\uAC00-\uD7A30-9a-zA-Z\s]','',page_text).replace("\n",'\s')
    r = r_t.replace('\\','')
    return r

def text_preprocessing2(page_text):
    r_t = re.sub('[^\uAC00-\uD7A3가-힣0-9a-zA-Z\.]','',page_text)
    r = re.sub('\n','',r_t)
    return r

def col_preprocessing(df,col_name):
    temp =[]
    for data in df[col_name]:
        pre_data = text_preprocessing(data)
        temp.append(pre_data)

    df[col_name] = temp

    return df 

def col_preprocessing2(df,col_name):
    temp =[]
    for data in df[col_name]:
        pre_data = text_preprocessing2(data)
        temp.append(pre_data)

    df[col_name] = temp

    return df 


def text_split(page_text):
    global common_require
    global require
    global job_main
    global pref

    if(page_text.find("공통 자격요건") != -1):
        if("공통 자격요건" in page_text):
            if(")" in page_text[page_text.find("공통 자격요건")+7:30]):
                common_require = page_text[page_text.find("공통 자격요건")+7:page_text.find("년)")+2]
            else:
                common_require = page_text[page_text.find("공통 자격요건")+7:page_text.find("관")+1]
                if("대졸 이상 (4년)S/W F/W 엔지니어S/W팀 0명담당업무" in page_text): 
                    # 특정공고 1개에서 에러 발생...
                    # 이유를 찾지못해서 string 으로 예외처리
                    common_require = page_text[page_text.find("공통 자격요건")+7:page_text.find("년)")+2]
                else:
                    common_require =""
            page_text = page_text[len("공통 자격요건")+len(common_require):]
    else:
       common_require =""  
    if("자격요건" in page_text):
        require = page_text[page_text.find('자격요건')+5:page_text.find("우대")]
    elif("지원자격" in page_text):
        require = page_text[page_text.find('지원자격')+5:page_text.find("우대")]
    else:
        require =''
    require = require.replace("\n","")
    require = require.replace("            ㆍ기타 필수 사항","")
    require = require.replace("및","없음")

    if(page_text.find("데이터 엔지니어") !=-1):
        lenght = len("데이터 엔지니어")
        page_text = page_text[page_text.find("데이터 엔지니어")+lenght:]
    elif(page_text.find("data engineer") != -1):
        lenght = len("data engineer")
        page_text = page_text[page_text.find("data engineer")+lenght:]
    else:
        pass
    
    if("담당업무" not in page_text):
        job_main ="정보 없음"
    else:
        job_main = page_text[page_text.find('담당업무')+5:page_text.find("자격")]
        if("우대" in job_main):
            job_main = page_text[page_text.find("담당업무")+5:page_text.find("우대")]

    if(len(job_main)<4):
        job_main = "정보없음"
    
    # 우대사항 
    # 원티드와 사람인의 구조가 다르기 떄문에 
    # 예외처리를 해주어야한다.
    try:
        pref = page_text[page_text.find('우대')+4:page_text.find('해택')]
    except:
        if ("해택" not in page_text ):
            if("기술스택" in page_text):
                pref = page_text[page_text.find('우대')+4:page_text.find('기술스택')]
        else:
            pref = "정보없음"

    
    return common_require,require,job_main,pref
    

