"""
Date : 22.04.27
Title : BAEKJOON 2438번
Project : 별 찍기 - 1
Level : Bronze 3
Name : thelight0804
"""
num = int(input())

for i in range(num):
    print('*')
    if (i != num-1): #if문을 쓰지 않는다면 for j를 한 번 더 실행하게 된다
        for j in range(i+1):
            print('*', end='')