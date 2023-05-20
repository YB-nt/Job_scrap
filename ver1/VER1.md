# Ver.1
<br>

**Use Skill :**  `reuqests`,`selenium`,`beutifullsoup4`,`psycopg2`,`postgreDB`,`konlpy`


<br>

## Data Extract
- requests+bs4m (Saramin)<br>
  - wanted에서 데이터를 새롭게 로딩을 시키기 위해서 `selenium`을 사용해서 동적스크래핑을 진행
- Selenium++bs4 (wanted)
  - Saramin에서 selenium 보다 속도가 빠르다고 생각하여 requests+bs4 를 사용해서  크롤링을 진행하였다.  
<br>

## Data Transform
-  크롤링해서 불러온 데이터를 split하는 방식으로 진행하였다. (퀵정렬을 생각하고 만들었다.) 
    - 데이터를 특정 키워드로 검색해서 나누고 이를 반복하는 방식으로 진행하였다.<br>
      문제점:수 많은 예외처리가 필요하였다.사람인 공고페이지들의 구조가 많이 다르기 떄문에, 문제가 발생 
    - 사람인과 원티드 각각 플랫폼마다 다르게 전처리 과정을 넣어 주었다.
<br>

## Data Load
- 전처리를 통해서 만들어진 정형데이터를 csv파일에서 postgreDB로 적재 진행해주었다. 
  - python을 이용해서 데이터베이스를 구성하고 적재하였다. 
<br>

## NLP
- konlpy를 통해서 추가적으로 불용어들 제거, 빈도수 분석 등을 진행하였다.
<br><br>
<br><br>
