"""
Pandas
파이썬에서 사용하는 데이터 분석 라이브러리
행과 열로 된 데이터 처리에 유용한 라이브러리
"""
import pandas as pd

# 1. Series
# 1차원 데이터(정수, 실수, 문자열 등)
# series 객체 생성
# 예) 1월 부터 4월 까지 평균 온도(-20,-10,10,20)

temp = pd.Series([-20,-10,10,20]) 
print(temp)

print(temp[0]) # 1월 온도
print(temp[2]) # 3월 온도


# series 객체를 만드는데 인덱스 지정하기
# 인덱스를 이용한 데이터 출력가능하다.
# 존재하지 않는 인덱스에 접근시 key error가 발생한다. 

temp = pd.Series([-20,-10,10,20], index=["Jan", "Feb", "Mar","Apr"])
print(temp) 
print(temp["Jan"])
