# job_scraping

## 프로잭트 배경
다양한 회사에서 다양한 기술들을 사용하고,또 많은 새로운 기술들이 나오고 있다. 
<br>
그래서 앞으로 공부를 진행하는데 가이드라인을 제시하기 위해서 
<br>
최근에 기업들이 많이 사용하는 기술들을 정리하기 위해서 해당 프로젝트를 생각하게 되었다. 
<br><br>

## 프로젝트 과정 
<br>

1. 데이터 수집 <br><br>
2. 데이터 전처리,변환 <br><br>
3. 데이터 저장 <br><br>
4. 데이터 검사  -  추가적인 데이터처리<br><br>
5. 데이터 시각화 - 데이터베이스에 저장되어있는 데이터들을 통해서 데이터에서 인사이트를 만들어 내기 <br><br>


<br><br><br>

# 프로젝트 상세내용
## Ver.1
<br>

**Use Skill :**  `reuqests`,`selenium`,`beutifullsoup4`,`psycopg2`,`postgreDB`,`konlpy`
<br><br>
### Data Extract
- requests+bs4m (Saramin)<br>
  - wanted에서 데이터를 새롭게 로딩을 시키기 위해서 `selenium`을 사용해서 동적스크래핑을 징핸
- Selenium++bs4 (wanted)
  - Saramin에서  requests+bs4 를 사용해서 selenium 보다 속도가 빠르다고 생각해서 requests+bs4를 사용해서 크롤링을 진행하였다.  
<br><br>
### Data Transform
-  크롤링해서 불러온 데이터를 split하는 방식으로 진행하였다. 퀵정렬을 생각하고 만들었다. 
    - 데이터를 특정 키워드로 검색해서 나누고 이를 반복하는 방식으로 진행하였다.<br>
      문제점:엄청나게 많은 예외처리가 필요하였다.;사람인 공고페이지들의 구조가 많이 다르기 떄문에, 문제가 발생 
    - 사람인과 원티드 각각 플랫폼마다 다르게 전처리 과정을 넣어 주었다.
<br><br>
### Data Load
- 전처리를 통해서 만들어진 정형데이터를 csv파일에서 postgreDB로 적재 진행해주었다. 
  - python을 이용해서 데이터베이스를 구성하고 적재를 진행하였다. 
<br><br>
### NLP
- konlpy를 통해서 추가적으로 불용어들 제거, 빈도수 분석 등을 진행하였다.
<br><br>
<br><br>

## Ver.2

### Crawling
- requests를 사용한 API호출(wanted)
- Scrapy(saramin,jobkorea)

<br><br>

**Use Skill :**  `urllib`,`scrapy`<br><br>
### 프로젝트 진행과정 
이전에 프로젝트를 진행하면서 selenium을 사용해성 동적으로 크롤링을 진행하다보니 페이지가 로딩되는데 많은 시간이 소요되어 속도가 다소 많이 아쉬운 부분이 있었다. 그래서 각 채용사이트별로 API를 확인하여 데이터를 불러오려고 하였다.<br>
- wanted(완성)
- 사람인,jobkorea(실패)

<br><br>
### 프로젝트 중단
기존의 생각했던 방식으로는 iframe과 다양한 문제들 때문에 크롤링을 정상적으로 진행하기 힘들다. 
다른 방법으로도 시도를 해보았지만 인코딩문제와 iframe처리에 한계성을  인해서 프로젝트를 중단하게 되었다.<br>

<br><br><br>

## Ver.3(진행중)
**Use Skill :**  `urllib`,`scrapy`,`MongoDB`
<br><br>
ver2에서 jobkorea 크롤링을 시도하였지만 실패하여서 가능한 사이트 위주로 진행하게 되었다. 
<br><br>
### 프로젝트에서 Scrapy를 사용한이유 
- selenium을 사용도 기능적으로 사용이 가능하고, 비동기성으로 크롤링을 진행하여 속도도 빠르며,다양한 추가 기능을 사용할 수 있어서 사용하게 되었다. 
<br><br><br><br>

### Data Extract
- requests를 사용한 API호출해서 데이터 저장(wanted)
    - 이전에 ver2에서 구현된것을 수정하여서 사용.
<br><br>
- ~~requests를 사용해서 API호출해서 데이터 저장(programmers)(중단)~~
  - 공고의 다양성이 적어서 제외<br><br><br>
- Scrapy(saramin) ver1+ver2+a
  - scrapy를 사용해서 ver1에서 사용했던 detail_page를 활용해서 scrapy를 사용해서 크롤링 진행
  - middleware를 추가하여서 크롤링 안정성을 높임
<br><br>
### Data Transform
  - 이전에 버전에서 가장 문제가 되었던 전처리 부분을 정규표현식을 사용하여 개선
  - 동의어 예외처리
  <br><br>
### Data Load
- scrapy의 파이프라인을 이용하여 mongodb와 연결후 데이터를 적재하였다.
- Mongodb에 데이터를 적재시 에러 발생하면 json으로 저장이 되도록 예외처리 진행하였다. 
<br><br><br><br>
### 앞으로 추가할 기능들
- ~~데이터 중복,누락 예외처리~~
- ~~데이터베이스 연동후 데이터베이스에 자동 저장~~

<br>

- 각 채용사이트 데이터 통합(진행중)
- Airflow
- 서버연동
- 데이터 시각화



