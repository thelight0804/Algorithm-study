"""
Date:
  22.12.14
Title:
  BAEKJOON 2292번
Project:
  벌집
Level:
  Bronze 2
Name:
  thelight0804
"""
standard_input = '13'

# input final number
final = int(input())
step = 1
count = 1

# go to step
while step < final:
  # move the step to the next box
  step += 6 * count
  count += 1

print(count)




# if (final == 1 or final == 2):
#   print(final)
# else:
#   for i in range(final):
#     if (step < final):
#       step += 6 * i
#     else:
#       print(i)
#       break

