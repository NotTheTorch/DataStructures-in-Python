class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        new_node = Node(data, None, itr)
        itr.next = new_node

    def insert_listValues_atEnd(self,dataset):
        for data in dataset:
            self.insert_at_end(data)

    def getLength(self):
        if self.head is None:
            return 0
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        print(count)
    
    def getLastNode(self):
        if self.head is None or self.head.next is None:
            return self.head
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_prev_value(self, data):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        while itr:
            if data == itr.data:
                if itr.prev is not None:
                    print(itr.prev.data)
                else:
                    print("This node is the head node and has no previous node.")
                return
            itr = itr.next
        
        print("Element not found in the list")

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        lstr = ""
        itr = self.head
        while itr:
            lstr += str(itr.data) + "-->"
            itr = itr.next
        lstr += "None"
        print(lstr)
    
    def print_backward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        lstr = ""
        itr = self.getLastNode()
        while itr:
            lstr += str(itr.data) + "-->"
            itr = itr.prev
        lstr += "head"
        print(lstr)

if __name__ == "__main__":
    dl = DoubleLinkedList()
    dl.insert_at_beginning(3)
    dl.insert_at_beginning(2)
    dl.insert_at_beginning(1)
    dl.insert_at_beginning(0)
    dl.get_prev_value(2)  
    dl.insert_listValues_atEnd(["blue","red","cyan"])
    dl.print_forward()
    dl.getLength()
    dl.getLastNode()
    dl.print_backward()