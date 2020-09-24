from Node import Node

class Stack:

    def __init__(self):
        "constructor to initiate this object"
        
        # store the first in the queue
        self.top = None
        # store the size of the queue
        self.size = 0

    def isEmpty(self):
        return self.top == None

    def Peek(self):
        return self.top.data

    def Push(self, data):
        if self.isEmpty():
            self.top = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode
        self.size +=1

    def Pop(self):
        if self.top is None:
            return None
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped
