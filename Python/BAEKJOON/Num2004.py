"""
Date:
  23.02.28
Title:
  BAEKJOON 2004번
Project:
  조합 0의 개수
Level:
  Silver 2
Name:
  thelight0804
"""
# standard_input = """25 12"""
# #2

# input n, m
n, m = map(int, input().split())

# counting number 2
def count2(n):
  cnt = 0
  while n >= 2:
    cnt += n//2
    n //= 2
  return cnt

# counting number 5
def count5(n):
  cnt = 0
  while n >= 5:
    cnt += n//5
    n //= 5
  return cnt

cnt5 = count5(n) - count5(m) - count5(n-m)
cnt2 = count2(n) - count2(m) - count2(n-m)

# output result
print(min(cnt5, cnt2))