"""
Date:
  23.05.08
Number:
  LeetCode 155
Title:
  Min Stack
Level:
  Medium
Name:
  thelight0804
"""

class MinStack(object):

  def __init__(self):
    self.stack = [] #normal stack
    self.minStack = [] #minimum element stack

  def push(self, val):
    """
    :type val: int
    :rtype: None
    """
    self.stack.append(val) #push

    #push minimum element
    if not self.minStack:
      self.minStack.append(val)
    elif val <= self.minStack[-1]:
      self.minStack.append(val)
      

  def pop(self):
    """
    :rtype: None
    """
    #pop minimum element
    if self.stack.pop() == self.minStack[-1]:
      self.minStack.pop()
      

  def top(self):
    """
    :rtype: int
    """
    return self.stack[-1]
      

  def getMin(self):
    """
    :rtype: int
    """
    return self.minStack[-1]
        