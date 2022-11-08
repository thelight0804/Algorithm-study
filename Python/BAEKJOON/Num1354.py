"""
Date:
    22.09.13
Title:
    BAEKJOON 1354번
Project:
    무한 수열 2
Level:
    Gold 5
Name:
    thelight0804
"""

#memoization
m = {}

def seq(num):
    if num < 1:
        return 1
    if num in m:
        return m[num]
    else:
        m[num] = seq(num//P-X) + seq(num//Q-Y)
    return m[num]

#input
num = list(map(int, input().split()))

N = num[0]
P = num[1]
Q = num[2]
X = num[3]
Y = num[4]

print(seq(N))