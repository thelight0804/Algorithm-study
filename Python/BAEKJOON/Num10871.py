"""
Date:
    22.10.28
Title:
    BAEKJOON 10871번
Project:
    X보다 작은 수
Level:
    Bronze 5
Name:
    thelight0804
"""

# standard_input = """
# 10 5
# 1 10 4 9 2 3 8 5 7 6
# """
#input
test, n = map(int, input().split(" "))
list = list(map(int, input().split(" ")))

#print less than n
for i in range(len(list)):
    if list[i] < n:
        print(list[i], end = ' ')