"""
Date:
    22.11.05
Title:
    BAEKJOON 2475번
Project:
    검증수
Level:
    Bronze 5
Name:
    thelight0804
"""
# standard_input = '1 2 3 4 5'

#input num
num = list(map(int, input().split(" ")))

#square num value
squr = list(map(lambda x: x**2, num))

#sum list
sum = sum(squr)

#print verification
print(sum % 10)