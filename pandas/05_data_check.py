"""
5. 데이터 확인
"""
import pandas as pd

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data, index=["1번", "2번","3번","4번","5번","6번","7번","8번"])
df.index.name = "지원번호"

df.to_csv("score.csv", encoding="utf-8-sig")


df = pd.read_csv("score.csv", index_col="지원번호")



# dataframe 확인
# 계산 가능한 데이터에 대해 column 별로 
# 갯수, 평균, 표준편차, 최소/최댓값 등의 정보를 보여준다. 
print(df.describe())

# 각 column에 대해 어떤 데이터 타입인지를 보여준다.
print(df.info())





# 처음 5개의 row를 가지고 온다.
# 숫자를 지정하면 지정된 숫자만큼 가지고 온다. default로는 5개를 가지고 온다
# print(df.head())
# print(df.tail())
# print(df.values)
# print(df.index)
# print(df.columns)
# print(df.shape) # 로우/컬럼 갯수를 알려준다.



# series확인
# print(df["키"].describe())
# print(df["키"].min())
# print(df["키"].max())
# print(df["키"].nlargest(3)) # 키 큰 사람 순서데로 3명의 데이터를 가지고 온다.
# print(df["키"].mean()) # 평균
# print(df["키"].sum())
# print(df["SW특기"].count())
# print(df["학교"].unique()) # 중복을 제거한 데이터 확인
# print(df["학교"].nunique()) # 중복을 제거한 데이터가 몇개인지 확인


