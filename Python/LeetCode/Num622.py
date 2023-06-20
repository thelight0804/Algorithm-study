"""
Date:
  23.06.20
Number:
  LeetCode 622
Title:
   Design Circular Queue
Level:
  Medium
Author:
  thelight0804
"""

class MyCircularQueue(object):
  def __init__(self, k):
    """
    :type k: int
    """
    self.arr = [None] * k #crate array
    self.head = 0 #first index
    self.tail = 0 #last index
    self.size = k #array length


  def enQueue(self, value):
    """
    :type value: int
    :rtype: bool
    """
    if self.arr[self.tail] is None: #Add data
      self.arr[self.tail] = value
      self.tail = (self.tail + 1) % self.size #move tail one step 
        #and prevent tail out of range
      return True
    else: #array is full
      return False


  def deQueue(self):
    """
    :rtype: bool
    """
    if self.arr[self.head] is not None: #pop data
      self.arr[self.head] = None
      self.head = (self.head + 1) % self.size #move head one step 
        #and prevent head out of range
      return True
    else: #array is empty
      return False
  

  def Front(self):
    """
    :rtype: int
    """
    if self.arr[self.head] is not None:
      return self.arr[self.head]
    else: #array is empty
      return -1
      

  def Rear(self):
    """
    :rtype: int
    """
    if self.arr[self.tail - 1] is not None:
      return self.arr[self.tail - 1]
    else: #array is empty
      return -1
      

  def isEmpty(self):
    """
    :rtype: bool
    """
    return self.arr[self.head] is None

      
  def isFull(self):
    """
    :rtype: bool
    """
    return self.arr[self.tail] is not None