"""
Date : 22.05.10
Title : BAEKJOON 2739번
Project : 구구단
Level : Bronze 3
Name : thelight0804
"""

num = int(input()) #입력 값

for i in range(9):
    mul = i+1 #곱할 값
    result = num*mul #곱셈 연산
    print(num, '*', mul, '=', result) #출력