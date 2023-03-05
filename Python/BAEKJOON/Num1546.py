"""
Date:
  22.11.17
Title:
  BAEKJOON 1546번
Project:
  평균
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input="""4
# 10 20 0 100
# """

#점수/M*100

#input test, scores
test = int(input())
score = list(map(int, input().split(' ')))

#find max score
maxScore = max(score)

#score / M * 100
score = list(map(lambda x: x/maxScore * 100, score))

#Average
avg = sum(score) / test

print(avg)