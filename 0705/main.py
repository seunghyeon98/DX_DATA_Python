# dir -> 이 함수가 iterator 인지, 아닌지를 확인할 수 있다.
data = 'hello'
dir(data)
'''
__ : 언버바가 붙어 있는 것은, 특수 메서드 이며, + 를 통해 호출할 수 있다.
'''

// 변경변경 //pull 해서 다시 commit


# help를 이용해서, sum에 대한 함수 설명 보기
help(sum)

# 파이썬 예약어 확인
import keyword
keyword.kwlist

# 모듈 순서 확인
import sys
sys.path
# (anaconda 설치시) pip install 하면, 'c:\\ProgramData\\anaconda3\\python310.zip' 경로에 설치된다.

year = 2023
print('윤년') if (year%400 ==0 or (year%100!=0 and year%4==0)) else print('윤년 아님')

'''

반올림 하고 싶은 자리를, 소수 첫 번째 자리로 옮기는 연습을 하고,
소수를 버리고 + 0.5하기

Q. 3750 을 10의 자리에서 반올림 해서 백의 단위로 변환

'''
#  37.5 + 0.5 = 38 -> int(38.0) -> 38
int(3750/100 + 0.5) *100
