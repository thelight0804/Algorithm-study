"""
Date:
    22.10.22
Title:
    BAEKJOON 14681번
Project:
    사분면 고르기
Level:
    Bronze 5
Name:
    thelight0804
"""
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")