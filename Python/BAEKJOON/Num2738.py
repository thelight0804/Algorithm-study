"""
Date:
    22.10.29
Title:
    BAEKJOON 2738번
Project:
    행렬 덧셈
Level:
    Bronze 5
Name:
    thelight0804
"""
standard_input="""3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
"""
#n, m input
n, m = map(int, input().split(" "))

#2d array initialization
a = [0 for i in range(n)]
b = [0 for i in range(n)]

#2d array input
for i in range(n):
    a[i] = list(map(int, input().split(" ")))

for i in range(n):
    b[i] = list(map(int, input().split(" ")))

#2d array sum and print
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
        print(a[i][j], end=" ")
    print()