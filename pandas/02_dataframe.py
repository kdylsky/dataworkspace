"""
DateFrame
series의 모음이라고 생각하면된다.
2차원 데이터(seies 들의 모음)

Data 준비
사전(dict) 자료구조를 통해 생성
예) 슬램덩크 주요 인물 8명에 대한 데이터
"""

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


# DataFrame 객체 생성

import pandas as pd

df = pd.DataFrame(data)

# 데이터 접근하기

print(df["이름"])
print(df["키"])

# 대괄호안에 리스트로 값을 넣어서 데이터를 가지고 온다.
print(df[["이름","키"]])

# DataFrame 객체 생성(인덱스 지정)
# 인덱스의 갯수가 다르면 오류가 난다.
df = pd.DataFrame(data, index = ["1번", "2번","3번","4번","5번","6번","7번","8번"])
print(df)

# DataFrame 객체생성(컬럼 지정해서 생성하기)
# 데이터 중에서 원하는 컬럼만 선택하거나 순서 변경가능
df = pd.DataFrame(data, columns=["이름", "학교","키"])
print(df)
df = pd.DataFrame(data, columns=["이름", "키","학교"])
print(df)


n = 25
k = 3

result = 0

while True:
    target = (n // k) * k # k로 나눌수 있는 가장 가까운 수를 찾는다.
    result += (n - target) # 연산을 수행하는 횟수
    n = target
    print(target,result)
    # 더이상 나눌 수 없을 때 반복문 탈출
    if n < k:
        break
    
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)