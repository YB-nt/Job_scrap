# Job Scrap

사용한 기술들 : `python`,`scrapy`,`mongodb`,`airflow` ...<br><br>


## 프로젝트 배경
다양한 회사에서 다양한 기술들을 사용하고,또 많은 새로운 기술들이 나오고 있다. 
<br>
그래서 앞으로 공부를 진행하는 데에 가이드라인을 제시하고
<br>
최근에 기업들이 많이 사용하는 기술들을 정리하기 위해서 해당 프로젝트를 생각하게 되었다. 
<br><br>

## 프로젝트 과정 

<br>

1. 데이터 수집 <br>
   - scrapy를 사용해서 데이터를 수집<br><br>
2. 데이터 전처리,변환<br>
   - 데이터를 정형데이터로 저장하기 위해서 문자열처리,정규표현식,nlp를 사용해서 데이터 변환<br><br>
3. 데이터 적제<br>
    - 주요 데이터 : 자격요건,우대사항,담당업무 ...<br>
    - 변환이 완료된 데이터를 mongodb(ver3),postgresql(ver1)에 적제<br><br>
    
<br><br><br>

# 프로젝트 상세과정 

### 프로젝트에서 Scrapy를 사용한이유 
- selenium을 기능적으로 사용이 가능 
- 비동기적으로 크롤링을 진행하여 속도도 빠르다.
- 다양한 추가 기능을 사용할 수 있다. middleware(auto-useragent,proxy setting ...)
<br><br>

## Data Extract
- middleware를 추가하여서 크롤링 안정성을 높여주었다.

- **wanted** <br>
  urllib로 데이터를 불러왔던 수집방식을 scrapy를 이용하여 
  ETL과정을 진행하도록 수정해주었다.

- **saramin** (ver1+ver2+a)
  - scrapy를 사용해서 ver1에서 사용했던 detail_page를 활용해서 scrapy를 사용해서 ETL 과정을 진행하였다.
  
<br>

## Data Transform
  - 이전에 버전에서 가장 문제가 되었던 전처리 부분을 정규표현식을 사용하여 개선
  - 동의어 예외처리
  <br><br>
## Data Load
- scrapy의 파이프라인을 이용하여 mongodb와 연결후 데이터를 적재하였다.
- Mongodb에 데이터를 적재시 에러 발생하면 json으로 저장이 되도록 예외처리 진행하였다. 

<br>



<br>

## workflow
- docker-compose 로 airflow 환경을 구성
- airflow를 사용해서 workflow를 구성 
- 매일 자정에 동작되도록 스케쥴링 해주었다. 

<br>

## TODO
- ~~데이터 중복,누락 예외처리~~
- ~~데이터베이스 연동후 데이터베이스에 자동 저장~~
- ~~wanted scrapy 로 변경~~
- ~~데이터베이스에 저장된데이터들 중복검사~~
- ~~Airflow + docker-compos~~
<br>

- 서버 연동<br>
- 데이터 시각화
- 추가적인 데이터 처리
- 크롤링 데이터 적합성 검사

<br>

## Before Version

- [ver1] https://github.com/YB-nt/Job_scrap/blob/main/ver1/README.md<br>
- [ver2] https://github.com/YB-nt/Job_scrap/blob/main/ver2/README.md<br>



