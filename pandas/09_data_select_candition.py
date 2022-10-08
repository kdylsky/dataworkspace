# 09. 데이터 선택(조건)
# 조건에 맞는 데이터를 가지고 오기

import pandas as pd
df = pd.read_csv("score.csv", index_col="지원번호")

# True or False로 알려준다.
df["키"] >= 190

# filter를 적용해서 데이터를 가지고 온다. 
filt = (df["키"] >= 185)
df[filt]

# filter에 적용되지 않는 데이터를 가지고 온다.
# ~ 키워드를 이용해서 적용시킨다.
# filter를 역으로 적용시킨다.
df[~filt]
df[df["키"]>=185]

#df.loc[row_selection, col_selection]
df.loc[ df["키"]>=185, "수학"]
df.loc[df["키"]>=185, ["이름", "수학", "과학"]]


## 다양한 조건
# & and 그리고 조건
filter_a = (df["키"] >= 185)
filter_b = (df["학교"] == "북산고")
df.loc[(df["키"] >= 185) & (df["학교"]== "북산고")]
df.loc[filter_a & filter_b]


# | or 또는 조건
filter_c = df["키"] > 200
filter_d = df["키"] < 170
df.loc[(df["키"] < 170)|(df["키"]>200)]
df.loc[filter_c | filter_d]



## str함수 
# string함수를 이용해서 문자열 비교

filt = df["이름"].str.startswith("송") # 특정 문자로 시작하는 데이터를 뽑는다.
df[filt]

filt = df["이름"].str.contains("태") # 특정문자를 포함하는 데이터를 뽑니다.
df[~filt]

langs = ["Python", "Java"]
filt = df["SW특기"].isin(langs) # 특기가 Python이거나 Java인 사람
df[filt]

langs = ["python","java"]
filt = df["SW특기"].str.lower().isin(langs)
df[filt]

filt = df["SW특기"].str.contains("java", na = False) #NaN 데이터에 대해서 True로 변경
filt = df["SW특기"].str.lower().str.contains("java", na = False) #NaN 데이터에 대해서 True로 변경
df[filt]

