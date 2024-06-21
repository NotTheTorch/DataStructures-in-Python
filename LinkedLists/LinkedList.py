class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_set):
        for data in data_set:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1

    def insert_value_after(self, data, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next
        raise ValueError(f"Element {data} not found in the list")
    
    def remove_by_value(self, data):
        if self.head is None:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr and itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        return
    
    def find_middle_node(self):
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def reverse_linked_list(self):
        itr = self.head
        prev = None
        while itr:
            temp = itr.next  
            itr.next = prev  
            prev = itr  
            itr = temp  
        self.head = prev
        return prev

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + " --> "
            itr = itr.next
        lstr += "None"
        print(lstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['apples', 'mangoes', 'grapes', 'oranges'])
    ll.remove_at(2)
    ll.insert_at(2, "figs")
    ll.print()
    print("Length of the linked list:", ll.get_length())
    print("Middle node:", ll.find_middle_node())
    ll.reverse_linked_list()
    ll.print()
