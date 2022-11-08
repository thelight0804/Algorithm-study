"""
Date : 22.05.05
Title : BAEKJOON 2562번
Project : 최댓값
Level : Bronze 2
Name : thelight0804
"""

big = 0 #최대값
count = 0 #최대값 카운트
tempCount = 0 #전체 카운트

for i in range(9):
    num = int(input())
    tempCount += 1 #전체 카운트 증가
    if(num > big): #입력되 값이 현재 최대값보다 크다면
        big = num
        count = tempCount
print(big)
print(count)