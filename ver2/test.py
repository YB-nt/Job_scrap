from urllib import parse
search_keyword="데이터 엔지니어"
target_url = parse.urlparse(f"https://www.jobkorea.co.kr/Search/?stext={search_keyword}")
query = parse.parse_qs(target_url.query)
url_query = parse.urlencode(query, doseq=True)
result_url ='https://www.jobkorea.co.kr/Search/?'+ url_query


print(result_url)