"""
Date:
  23.04.04
Problem:
  BAEKJOON 1018번
Project:
  체스판 다시 칠하기
Level:
  Silver 4
Author:
  thelight0804
"""

# standard_input = """8 8
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB"""
# #12

#input n, m
n, m = map(int, input().split())
#input board
board = [input() for _ in range(n) ]
cnt = []

#cut 8*8 boards
for i in range(n-7):
  for j in range(m-7):
    white = 0
    black = 0
    #check W, B from row * col
    for k in range(i, i+8):
      for l in range(j, j+8):
        if (k + l) % 2 == 0: #Even
          if board[k][l] == 'W':
            black += 1
          if board[k][l] == 'B':
            white += 1
        else: #odd
          if board[k][l] == 'B':
            black += 1
          if board[k][l] == 'W':
            white += 1
    #add cnt
    cnt.append(white)
    cnt.append(black)

#output minimum
print(min(cnt))