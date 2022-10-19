import re

text = """        우대사항데이터사이언티스트 0명담당업무ㆍ[담당업무]ㆍ쇼핑플랫폼의 Front-end AI 시스템 개발 (Optimization,CF,FM)ㆍ가격
비교플랫폼의 Back-end AI 시스템 개발 (NLP,CNN,RNN)[자격요건]ㆍ경력 : 신입 ~ 3년이하ㆍ원활한 커뮤니케이션 능력으로 차분히 논 
리를 전개하실 수 있는 분ㆍMachine Learning관련 학위 혹은 관련된 프로젝트 경험이 있으신 분ㆍ수작업을 자동화하고 업무를 효율화
 하면서 끊임 없는 성능개선에 즐거움을 느끼시는 분ㆍ데이터를 가공/시각화하고 이를 분석하여 인사이트를 얻고 설득하는 것에 즐거
움을 느끼시는 분[우대사항]ㆍ R,Python,C++ 중 한가지 언어를 능숙하게 다루시는 분ㆍ Keras(Tensorflow) 기반의 NLP분야의 Deep Learning 경험이 있으신 분ㆍ Kaggle 등 머신러닝 대회 참가 경험이 있으신 분
"""

p=re.compile("(?<=\])(.*?)(?=<\[)")
# p= re.compile('[\r\n\v]')
result = p.findall(text)
print(result)
# for _ in p.finditer(text):
#     print()
#     print(text[_.start():])



