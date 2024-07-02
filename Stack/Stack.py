from collections import deque

class Stack:
    def __init__(self):
        self.buffer = deque()
    
    def push(self,data):
        self.buffer.append(data)
    
    def deleteValue(self):
        self.buffer.pop()

    def getLength(self):
        return len(self.buffer)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(5)
stack.push(6)
print(stack.buffer)
stack.deleteValue()
print(stack.buffer)
print(stack.getLength())