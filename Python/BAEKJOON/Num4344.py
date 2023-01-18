"""
Date:
  23.01.04
Title:
  BAEKJOON 4344번
Project:
  평균은 넘겠지
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input = """5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91"""

#input number
test = int(input())
for i in range(test):
  num = list(map(int, input().split()))
  student = num[0]

  #calculate average
  avg = sum(num[1:]) / student

  #check students score above average
  count = 0
  for j in range(student):
    if(num[j+1] > avg):
      count +=1

  #print result
  rate = count / student * 100
  print(f'{rate:.3f}%')