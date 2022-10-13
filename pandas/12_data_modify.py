# 데이터 수정

import pandas as pd
df = pd.read_csv("score.csv", index_col="지원번호")


# 컬럼수정
df["학교"].replace({"북상고":"무슨고"})
df["학교"].replace({"북상고":"무슨고"}, inplace=True)


df["SW특기"].str.lower()
df["SW특기"] = df["SW특기"].str.lower()
df["SW특기"] = df["SW특기"].str.upper()

df["학교"] = df["학교"] + "등학교"



# 컬럼추가
df["총합"] = df["국어"] + df["영어"] + df["수학"] + df["과학"] + df["사회"]
df["결과"] = "Fail"

# 총합이 400보다 큰 데이터에 대해서 결과를 pass로 업데이트
df.loc[df["총합"]>400, "결과"] = "pass"



# 컬럼삭제

df.drop(columns=["총합"])
df.drop(columns=["국어","영어","수학"]) # inplace




# 로우 삭제
df.drop(index="4번") # inplace

# 조건 삭제
filt = df["수학"] < 80
df[filt].index
df.drop(index = df[filt].index)


# 로우 추가
df.loc["9번"] = ["이정환","해남고등학교", 184, 90, 90, 90, 90, 90, "Kotlin", 450, "Pass"]


# cell 수정
df.loc["4번", "SW특기"] = "Python"
df.loc["5번", ["학교", "SW특기"]] = ["능남고등학교", "C"]


# 컬럼 순서 변경
cols = list(df.columns)
df = df[[cols[-1]]+ cols[0:-1]] # 맨뒤의 결과 컬럼을 맨 앞으로 가지고 온다.



# 컬럼의 이름 변경
# df.columns =["result", "name","school"]
# 컬럼 갯수와 바꾸고자 하는 리스트 내의 갯수가 같아야 한다.