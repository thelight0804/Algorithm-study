"""
Date:
  23.06.20
Number:
  LeetCode 232
Title:
  Implement Queue using Stacks
Level:
  Easy
Author:
  thelight0804
"""

####Use deque
from collections import deque

class MyQueue(object):

  def __init__(self):
    self.queue = deque()


  def push(self, x):
    """
    :type x: int
    :rtype: None
    """
    self.queue.append(x)
      

  def pop(self):
    """
    :rtype: int
    """
    return self.queue.popleft()
      

  def peek(self):
    """
    :rtype: int
    """
    return self.queue[0]
      

  def empty(self):
    """
    :rtype: bool
    """
    # print(len(self.queue))
    return len(self.queue) == 0



####Use stack(list)
class MyQueue(object):

  def __init__(self):
    self.stack = []


  def push(self, x):
    """
    :type x: int
    :rtype: None
    """
    self.stack.append(x)
      

  def pop(self):
    """
    :rtype: int
    """
    val = self.stack[0]
    self.stack = self.stack[1 : len(self.stack)]
    return val
      

  def peek(self):
    """
    :rtype: int
    """
    return self.stack[0]
      

  def empty(self):
    """
    :rtype: bool
    """
    return len(self.stack) == 0