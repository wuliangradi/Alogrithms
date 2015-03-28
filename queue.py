#!/usr/bin/env python
#_*_coding:utf-8_*_

class Queue:
     def __init__(self):
         self.items = []

     def size(self):
         return len(self.items)

     def ifEmpty(self):
         return self.items == []

     def enqueue(self, item):
         self.items.append(item)

     def dequeue(self):
         if self.ifEmpty():
             return False
         else:
             return self.items.pop(0)
     def getElements(self):
         return self.items

q = Queue()
q.enqueue(9)
q.enqueue(10)
q.enqueue(3)
print q.getElements()