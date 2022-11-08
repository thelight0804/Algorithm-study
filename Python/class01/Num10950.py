"""
Date:
    22.05.18
Title:
    BAEKJOON 10950번
Project:
    최소, 최대
Level:
    Bronze 3
Name:
    thelight0804
"""

# 반복횟수 입력
roopNum = int(input())

#덧셈 연산 반복
for i in range(roopNum):
    str = input() #두 수 입력

    # 숫자 분리
    strList = [int(i) for i in str.split(' ')] 

    #숫자 분배
    a = strList[0]
    b = strList[1]

    print(a+b)