"""
Date:
  2023.05.23
Title:
  Linked List class
Author:
  thelight0804
"""


#Node 객체
class ListNode: #새로운 Node 생성
  def __init__(self, value):
    self.value = value #데이터 값
    self.next = None #다음 node 주소

#Linked list 출력
def printNodes(node:ListNode):
  crntNode = node #현재 node
  while crntNode is not None:
    print(crntNode.value, end=" ") #현재 node value 출력
    crntNode = crntNode.next #다음 node 이동

#LinkedList 객체
class SLinkedList:
  def __init__(self): #첫 node 생성자
    self.head = None

  #Add node at head
  def addAtHead(self, value): # O(1)
    newNode = ListNode(value) #새 노드 생성
    newNode.next = self.head #끝 주소 설정
    self.head = newNode #추가 노드를 head로 지정
  
  #Add node at tail
  def addBack(self, value): # O(n)
    newNode = ListNode(value) #새 노드 생성
    crntNode = self.head #현재 탐색중인 노드
    # while crntNode.next != None: #끝 노드로 이동
    while crntNode.next: #끝 노드로 이동
      crntNode = crntNode.next
    crntNode.next = newNode #노드 연결
  
  #found node value in linked list
  def findNode(self, value): # O(n)
    crntNode = self.head #현재 탐색중인 노드
    while crntNode != None: #노드 탐색
      if crntNode.value == value: #탐색 성공
        return crntNode
      crntNode = crntNode.next #다음 노드 이동
    raise RuntimeError("Node not found") #탐색 실패
  
  #add node at next node
  def addAfter(self, node, value): # O(1)
    newNode = ListNode(value) #새 노드 생성
    newNode.next = node.next #새 노드 주소 연결
    node.next = newNode #기존 노드를 새 노드 주소로 연결

  #delete next node
  def deleteAfter(self, node): # O(1)
    if node.next != None:
      node.next = node.next.next
    

slist = SLinkedList()
slist.addAtHead(1)
slist.addAtHead(2)
slist.addBack(3)

node1 = slist.findNode(1)
slist.addAfter(node1, 4)

slist.deleteAfter(node1)

printNodes(slist.head)
# #Node not found
# node2 = slist.findNode(5)
# print(node2.value)
