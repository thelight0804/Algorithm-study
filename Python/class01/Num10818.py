"""
Date : 22.05.15
Title : BAEKJOON 10818번
Project : 최소, 최대
Level : Bronze 3
Name : thelight0804
"""
repeatNum = int(input()) #입력 개수
inputNum = input() #입력 값

#int형 list
Num = [int(i) for i in inputNum.split(' ')]

max = min = Num[0] #최대, 최소 초기화

#연산
for i in range(len(Num)):
    if(Num[i] > max):
        max = Num[i]
    elif(Num[i] < min):
        min = Num[i]

    # max if Num[i] > max else min if Num[i] < min [Error]

print(min, max)