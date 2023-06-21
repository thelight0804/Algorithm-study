"""
Date:
  2023.06.18
Title:
  Queue class
Author:
  thelight0804
"""

#Queue Node 클래스
class QueueNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

#Queue 클래스
class Queue:
  #Queue constructor
  def __init__(self):
    self.head = QueueNode(0)
    self.tail = QueueNode(0)
    self.head.right = self.tail
    self.tail.left = self.head
  
  #enqueue
  def enqueue(self, value):
    newNode = QueueNode(value) #node 생성
    lastNode = self.tail.left #이전 노드
    #왼쪽 연결
    lastNode.right = newNode
    newNode.left = newNode

    #오른쪽 연결
    self.tail.left = newNode
    newNode.right = self.tail
  
  #dequeue
  def dequeue(self):
    firstNode = self.head.right
    if firstNode == self.tail: #queue가 비어있을 때
      return RuntimeError("empty queue")

    value = firstNode.value #값 저장
    #두번째 노드 연결
    secondNode = firstNode.right
    self.head.right = secondNode
    secondNode.left = self.head

    return value #값 반환

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue()) #empty queue