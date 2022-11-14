from konlpy.tag import Okt
import pandas as pd



df = pd.read_csv('../csv/saramin.csv')
data = df['job_section']

okt = Okt()
for i in data:
    print(okt.nouns(str(i)))




