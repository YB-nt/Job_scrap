# Ver.3(진행중)
**Use Skill :** `scrapy`,`MongoDB`
<br><br>
ver2에서 jobkorea 크롤링을 시도하였지만 실패하여서 가능한 사이트 위주로 진행하게 되었다. 
<br><br>

## 프로젝트에서 Scrapy를 사용한이유 
- selenium을 기능적으로 사용이 가능하고, 비동기성으로 크롤링을 진행하여 속도도 빠르며,다양한 추가 기능을 사용할 수 있기 때문에 사용하게 되었다. 
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
<br><br><br>


## 앞으로 추가할 기능들
- ~~데이터 중복,누락 예외처리~~
- ~~데이터베이스 연동후 데이터베이스에 자동 저장~~
- ~~wanted scrapy 로 변경~~
- ~~데이터베이스에 저장된데이터들 중복검사~~
<br>

- Airflow + docker-compose

<br>
- 서버 연동<br>
- 데이터 시각화



