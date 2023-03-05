"""
Date:
  23.01.21
Title:
  BAEKJOON 1924번
Project:
  2007년
Level:
  Bronze 1
Name:
  thelight0804
"""
standard_input = """12 1"""

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0

#input month, day
a, b = map(int, input().split())

# add day of month
for i in range(a-1):
  day += month[i]

# add input day
day = (day+b)%7
print(week[day])





# #input month and day
# month, day = map(int, input().split())

# # Jan, Feb
# if(month == 1):
#   print(week[(day%7)])
# elif(month == 2):
#   if(day < 4):
#     day += 3
#   # avoid list index out of range
#   else:
#     day -= 4
#   print(week[(day%7)])
# else:
#   # as month pass, add 2 or 3 days space
#   for i in range(2, month):
#     if(i == 3 or i == 5 or i == 7
#       or i == 8 or i == 10 or i == 12):
#       day += 3
#     else:
#       day += 2
#   print(week[(day+1)%7])