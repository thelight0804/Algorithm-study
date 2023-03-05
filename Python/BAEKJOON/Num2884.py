"""
Date:
  22.11.13
Title:
  BAEKJOON 2884번
Project:
  알람 시계
Level:
  Bronze 3
Name:
  thelight0804
"""
# standard_input = '23 40'

#input hour and minute
hour, minute = map(int, input().split(" "))

#minus 45 form minute
minute -= 45

# Calculate time of 60 minute
if minute < 0:
  minute += 60
  hour -= 1

# Calculate time of 12 hour
if hour == -1:
  hour = 23

print(hour, minute)