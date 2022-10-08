# 10. 결측치
# 비어있는 데이터를 의미한다. 
# Nan등을 결측치라고 한다.

import pandas as pd
df = pd.read_csv("score.csv", index_col="지원번호")


# 데이터 채우기 fillina
df.fillna("") # NaN데이터를 빈칸으로 채운다.
df.fillna("없음") # NaN데이터를 빈칸으로 채운다.

import numpy as mp
df["학교"] = mp.nan
df.fillna("모름", inplace=True) # 데이터프레임 전체에 대해서 적용이 된다. , 적용을 시키려면 inplace옵션을 주어야 한다.


df = pd.read_csv("score.csv", index_col="지원번호")
df["SW특기"].fillna("확인중")
df["SW특기"].fillna("확인중", inplace=True)


# 데이터 제외하기 dropna
df = pd.read_csv("score.csv", index_col="지원번호")
df.dropna(inplace=True) # NaN 데이터를 포함하는 데이터를 삭제 NaN을 포함하면 무조건 삭제



df = pd.read_csv("score.csv", index_col="지원번호")
# axis 속성 : index or columns
# how 속성  : any or all 
df.dropna(axis="index", how = "any") # NaN이 하나라도 있으면 row 을 삭제
df.dropna(axis="columns", how = "any") # NaN이 하나라도 있는 column을 삭제

df["학교"] = mp.nan
df.dropna(axis="columns", how = "all") # 데이터 전체가 NaN인 경우에만 Column 삭제