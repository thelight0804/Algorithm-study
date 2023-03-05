"""
Date:
    22.07.19
Title:
    BAEKJOON 1978번
Project:
    소수 찾기
Level:
    Silver 5
Name:
    thelight0804
"""
numCount = int(input())
number = list(map(int, input().split()))
count = 0 #소수 개수

#소수 찾기
for i in range(len(number)):
  #소수 확인 카운트
  prime = 0
  for j in range(2, number[i]+1):
    if(number[i] % j == 0):
      prime += 1
  #prime이 1개만 나와야 소수로 인정한다
  if(prime == 1):
    count += 1
print(count)