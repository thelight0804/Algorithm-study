"""
Date:
  23.03.02
Title:
  BAEKJOON 4949번
Project:
  균형잡힌 세상
Level:
  Silver 4
Name:
  thelight0804
"""
# standard_input = """So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
# ])
#  .
# ."""
# yes
# yes
# no
# no
# no
# yes
# yes

while True:
  str = input()

  #exit loop
  if str == '.': break

  else:
    s = []
    for i in str:
      if i == '(' or i == '[': #open brackets
        s.append(i)
      elif i == ')': #close bracket
        if not s or s[-1] != '(': #not balanced
          s.append(i)
          break
        else: s.pop() #delete brackets
        
      elif i == ']': #close bracket
        if not s or s[-1] != '[': #not balanced
          s.append(i)
          break
        else: s.pop() #delete brackets

    if len(s) == 0: print("yes")
    else: print("no")