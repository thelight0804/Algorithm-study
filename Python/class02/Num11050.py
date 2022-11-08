"""
Date:
    22.07.14
Title:
    BAEKJOON 11050번
Project:
    이항 계수 1
Level:
    Bronze 1
Name:
    thelight0804
"""

#숫자 입력
str = input()
strList = [int (i) for i in str.split(' ')]
n = strList[0]
k = strList[1]

#분모, 분자 변수 선언
down = 1 #분자
up = 1 #분모

downTemp = n-k #분자 임시 변수

#분모 계산
for i in range(k, 1, -1):
  down *= i
for i in range(downTemp, 1, -1):
  down *= i

for i in range(n, 1, -1):
  up *= i

#결과값 출력
print(int(up/down))