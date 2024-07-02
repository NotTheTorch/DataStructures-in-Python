from collections import deque

class Queue:
    def __init__(self) :
        self.buffer = deque()
    
    def enqueue(self,data):
        self.buffer.appendleft(data)
    
    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return (len(self.buffer) == 0)
    
    def Size(self):
        return len(self.buffer)
    

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.buffer)
print("Size of the queue:",queue.Size())

print(queue.dequeue(),"is popped")
print("Queue is Empty:",queue.isEmpty())
