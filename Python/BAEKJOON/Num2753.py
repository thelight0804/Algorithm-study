"""
Date:
    22.10.22
Title:
    BAEKJOON 2753번
Project:
    윤면
Level:
    Bronze 5
Name:
    thelight0804
"""
year = int(input())

if (year % 100 != 0 or year % 400 ==0) and year % 4 == 0:
    print("1")
else:
    print("0")