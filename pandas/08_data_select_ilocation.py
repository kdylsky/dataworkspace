# 8.데이터 선택(iloc)
# 정수데이터를 이용한 데이터 선택
# 위치를 이용해서 원하는 row에서 원하는 col선택

import pandas as pd
df = pd.read_csv("score.csv", index_col="지원번호")

df.iloc[1] # 인덱스에 해당하는 데이터를 가지고 온다.
df.iloc[0:5] # 일반 슬라이싱으로 맨마지막을 포함하지 않는다.

df.iloc[0,1] # 로우의 0번째 위치의 컬럼의 1번째 데이터
df.iloc[4,2] 

df.iloc[[1,2],2] # 1개 이상의 로우의 특정 컬럼의 데이터 가지고 오기
df.iloc[[1,2],[3,4]]
df.iloc[0:5, 3:8] #슬라이싱을 이용한 원하는 로우에서 원하는 컬럼을 가지고 오기
