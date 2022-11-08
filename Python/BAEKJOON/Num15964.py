"""
Date:
    22.11.05
Title:
    BAEKJOON 15964번
Project:
    이상한 기호
Level:
    Bronze 5
Name:
    thelight0804
"""
#A＠B = (A+B)×(A-B)
# standard_input = '3 4'

#input a and b
a, b = map(int, input().split(" "))

print((a+b)*(a-b))