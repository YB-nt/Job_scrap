from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 데이터 로드
data = pd.read_csv("../data/data.csv", encoding='utf-8')

# TfidfVectorizer 객체 생성
vectorizer = TfidfVectorizer(max_features=1000)

# 텍스트 데이터 벡터화
X = vectorizer.fit_transform(data['text'].values)

# KMeans 객체 생성
kmeans = KMeans(n_clusters=5, random_state=0)

# KMeans 알고리즘 적용
kmeans.fit(X)

# 클러스터링 결과 출력
for i in range(5):
    cluster = data[kmeans.labels_ == i]['text'].values
    print(f"Cluster {i}: {cluster}")
