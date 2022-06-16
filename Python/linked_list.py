# hackerrank linked-list problem solution
# problem link --- > https://www.hackerrank.com/challenges/30-linked-list/problem?isFullScreen=true

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):  # solution here
    #Complete this method
      if head == None:
        head = Node(data)
      else:
        current = head                # solution function here
        while current.next:           #  - other classes and funcs had already been given
          current = current.next
        current.next = Node(data)
      return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 

#check out the source code - and problem page on hackerrank link below

#### https://www.hackerrank.com/challenges/30-linked-list/problem?isFullScreen=true
