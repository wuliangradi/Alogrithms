#!/usr/bin/env python
#_*_coding:utf-8_*_

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def ifEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return None

    def getElements(self):
        return self.items

e = Stack()
e.push(5)
e.push(6)
print e.getElements()
e.pop()
print e.getElements()
print e.ifEmpty()
