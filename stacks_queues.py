#creating stack using list
l=[]
l.append(1)
l.append(2)
l.append(3)
print(l)
l.pop()
l.pop()
print(l)
'----------------------------------------------------------------'
#creating stack using collection.deque
#follows LIFO and FIFO
from collections import deque
l=deque()
l.append(1)
l.append(2)
l.append(3)
print(l)
l.pop()
l.pop()
print(l)
'-------------------------------------------------------------------------'
#creating stack using LifoQueue
#it only followe LIFO
from queue import LifoQueue
l=LifoQueue()
l.put(1)
l.put(2)
l.put(3)
print(l)
l.get()
l.get()
print(l)
'-------------------------------------------------------------------------'
#__str__()
class main:
    def __init__(self,name,email,num):
        self.name=name
        self.email=email
        self.num=num
    def __str__(self):
        s='name:{},email{},num{}'
        x=s.format(self.name,self.email,self.num)
        return x
n=input()
e=input()
num=int(input())
obj=main(n,e,num)
print(obj)
        
'---------------------------------------------------------------------------------'
#creating stack using linkedlist
class Node:
    def __init__(self,d):
        self.d=d
        self.next=None
class stack:
    def __init__(self):
        self.head=Node('none')
        self.size=0
    def push(self,d):
        node=Node(d)
        node.next=self.head
        self.head=node
        self.size+=1
    def __str__(self):
        cur=self.head.next
        out=""
        while cur:
            out+=str(cur.d)+"->"
            cur=cur.next
        return out[:-2]
    def pop(self):
        remove=self.head.next
        self.head=remove
        self.size-=1
    def isEmpty(self):
        return self.size == 0
    def peek(self):
        x=self.head.next.d
        return x
if __name__ == '__main__':
    s=stack()
    for i in range(1,11):
        s.push(i)
    print(f"stack:{s}")
    for i in range(1,6):
        s.pop()
    print(f"stack:{s}")
    print(s.isEmpty())
    print(s.peek())
'-----------------------------------------------------------------------------------------------'
#creating queue using list
l=[]
l.append(1)
l.append(2)
l.append(3)
print(l)
l.pop(0)
l.pop(0)
print(l)
'----------------------------------------------------------------------------------------------'
#creating stack using collection.deque
#follows LIFO and FIFO
from collections import deque
l=deque()
l.append(1)
l.append(2)
l.append(3)
print(l)
l.popleft()
l.popleft()
print(l)
'-------------------------------------------------------------------------------------------------'
#creating stack using LifoQueue
#it only followe LIFO
from queue import LifoQueue
l=LifoQueue()
l.put(1)
l.put(2)
l.put(3)
print(l)
print(l.get())
print(l.get())
print(l)
'-----------------------------------------------------------------------------------------------------'
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Queue:
    
    def __init__(self):
        self.rear=None
        self.front=None
        
    def isEmpty(self):
        return self.front is None and self.rear is None
        
    def enqueu(self,data):
        node=Node(data)
        if self.rear is None:
            self.rear = self.front = node
        self.rear.next=node
        self.rear=node
        
    def dequue(self,data):
        if self.isEmpty():
            print("underflow")
        temp=self.front
        self.fronnt=self.front.next
        if self.front is None:
            self.rear = None
            
    def get_front(self):
        return self.front.data
        
    def get_rear(self):
        return self.rear.data
    def __str__(self):
        cur=self.front
        out=""
        while cur:
            out+=str(cur.data)+"->"
            cur=cur.next
        return out
        
if __name__ == '__main__':
    q=Queue()
    q.enqueu(1)
    q.enqueu(2)
    q.enqueu(4)
    print(q.get_front())
    print(q.get_rear())
    print(q)
'-----------------------------------------------------------------------------------------'
