"""
3.index
데이터에 접근할 수 있는 주소값이다.
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

df = pd.DataFrame(data, index = ["1번", "2번","3번","4번","5번","6번","7번","8번"])
print(df.index)

## index 이름 설정
df.index.name = "지원번호"
print(df)

## index 초기화, 실제 데이터에는 반영이 안된다. inplace= True는 실제 데이터에 적용하는 것이다.
df.reset_index(inplace=True)
print(df)

df.reset_index(drop=True, inplace=True) # 원래 쓰던 "지원번호" 인덱스 삭제
print(df)

# index설정 
# 지정한 column으로 index를 설정

df.set_index("이름", inplace=True)
print(df)


## index정렬
# index를 기준으로 오름차순, 내림차순 정렬
# 오름차순
df.sort_index() # inplace = True 설정하지 않으먄 정렬된 값이 반영되지 않는다.

# 내림차순
df.sort_index(ascending=False)

