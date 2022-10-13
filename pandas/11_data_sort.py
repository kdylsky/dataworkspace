# 데이터 정렬

import pandas as pd
df = pd.read_csv("score.csv", index_col="지원번호")


# 하나를 기준으로 정렬
# 키 기준으로 오름차순 정렬
df.sort_values("키", ascending=False)
# 키 기준으로 내림차순 정렬
df.sort_values("키", ascending=False)



# 여러개를 기준으로 정렬
# 같은 경우 두번째 요소로 정렬을 하게 된다.
df.sort_values(["수학","영어"], ascending=False)

# 각각의 요소에 대해서 오름차순, 내림차순을 정할 수 있다.
df.sort_values(["수학","영어"], ascending=[True, False])


# 시리즈에 대해서 정렬을 할 수 있다.
df["키"].sort_values()


# 인덱스를 이용해서 정렬을 할 수 있다.
df.sort_index()
df.sort_index(ascending=False)