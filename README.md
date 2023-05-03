# job_scraping

## Ver1

### Crawling
- Selenium (Saramin)
- requests+bs4 (wanted)
### Database
- postgreDB
### NLP
- konlpy
<br><br><br>


## Ver2

### Crawling
- requests를 사용한 API호출(wanted)
- Scrapy(saramin,jobkorea)

### 프로젝트 중단
기존의 생각했던 방식으로는 iframe과 다양한 문제들 때문에 크롤링을 정상적으로 진행하기 힘들다. 
다른 방법으로도 시도를 해보았지만 인코딩문제로 인해서 프로젝트를 중단하게 되었다.

<br><br><br>
## Ver3(진행중)

### Crawling
- requests를 사용한 API호출(wanted)
- Scrapy(saramin) ver1+ver2+a
  - scrapy를 사용해서 ver1에서 사용했던 detail_page를 활용해서 scrapy를 사용해서 크롤링 진행
 
### Data Load
- json


### 앞으로 추가할 기능들
- ~~ 데이터 중복,누락 예외처리 ~~
- 데이터베이스 연동후 데이터베이스에 자동 저장(진행중)
- Airflow
- 서버연동
- 데이터 시각화(metabase)



