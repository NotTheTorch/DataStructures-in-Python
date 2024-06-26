class Node:
    def __init__(self,data=None,next=None) :
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) :
        self.head = None

    def appendValues(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data,None)

    def oddEven(self):
        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head

        return self.head



    def printLinkedList(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        ListString = ""
        
        curr = self.head

        while curr:
            ListString += str(curr.data) + "-->"
            curr = curr.next
        
        ListString += "None"
        print(ListString)



if __name__ == "__main__":
    ll = LinkedList()
    ll.appendValues(1)
    ll.appendValues(2)
    ll.appendValues(3)
    ll.appendValues(4)
    ll.appendValues(5)
    ll.appendValues(6)
    ll.printLinkedList()
    ll.oddEven()
    ll.printLinkedList()