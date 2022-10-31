def data_scaling(page_text):
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
                    pass
    page_text = page_text[len("공통 자격요건")+len(common_require):]
    if("자격요건" in page_text):
        require = page_text[page_text.find('자격요건')+5:page_text.find("우대")]
    elif("지원자격" in page_text):
        require = page_text[page_text.find('지원자격')+5:page_text.find("우대")]

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
