#Linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
#insert at beg
    def insert_at_beg(self,data):
        new_node=Node(data)#creating a node
        new_node.next=self.head #assigning new_node address to head
        self.head=new_node#changing new_node as head
        print("done insertion starting")
        
#insert at end
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:#checking if node is empty or not
            self.head=new_node
            return
        last_node=self.head
        while last_node.next: #traverse to last node
            last_node=last_node.next
        last_node.next=new_node
        print("done insertion ending")
#insert at random   
    def random_insert(self,data,pos):
        new_node=Node(data)
        if(pos==0):
            new_node.next=self.head
            self.head=new_node
            return
        current =self.head
        for i in range(pos-1):
            if current is None:
                print("None")
                return 
            current=current.next
        if current is None:  # Check if the position is valid
            print("Position out of bounds")
            return
        new_node.next=current.next
        current.next=new_node
        print("done insertion specific")
#delete at first
    def delete_at_start(self):
        if self.head is None:
            print("Empty list")
            return
        self.head=self.head.next
        print("done")
#delete at last
    def delete_at_last(self):
        if self.head is None:
            print("empty list")
            return
        if self.head.next is None:
            self.head=None
            return
        second_ln=self.head
        while second_ln.next.next:
            second_ln=second_ln.next
        second_ln.next=None
        print("Done")
#delete specific value
    def del_value(self,value):
        if self.head is None:
            print("empty list")
            return
        if self.head.data == value:
            self.head=self.head.next
            print("done")
            return
        current=self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                print("done")
                return 
            current= current.next
    def search(self,value):
        current=self.head
        index=0
        while current:
            if current.data == value:
                print(" value found at : ",index)
                return True
            current=current.next
            index+=1
        print("not found")
#display
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
        print("none")
if __name__ == "__main__":
    sll=LinkedList()
    sll.insert_at_beg(10)
    sll.insert_at_beg(11)
    sll.insert_at_end(20)
    sll.insert_at_end(22)
    sll.random_insert(30,2)
    sll.delete_at_start()
    sll.delete_at_last()
    sll.insert_at_beg(11)
    sll.insert_at_beg(21)
    sll.del_value(20)
    sll.display()
    sll.search(30)
'-------------------------------------------------------------------------------------------------'
#Double_linked_list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        print("done insertion at beginning")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print("done insertion at end")
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        print("done insertion at end")

    def random_insert(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            print("done insertion at specific position")
            return
        
        current = self.head
        for i in range(pos - 1):
            if current is None:
                print("Position out of bounds")
                return 
            current = current.next
        
        if current is None:
            print("Position out of bounds")
            return
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        print("done insertion at specific position")

    def delete_at_beg(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        print("done deletion at beginning")

    def delete_at_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        
        if self.head.next is None:  # Only one node
            self.head = None
            print("done deletion at end")
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.prev.next = None  # Remove the last node
        print("done deletion at end")

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        
        # If the node to delete is the head
        if self.head.data == value:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            print(f"done deletion of value {value}")
            return
        
        current = self.head
        while current:
            if current.data == value:  # Found the node to delete
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                print(f"done deletion of value {value}")
                return
            current = current.next
        
        print(f"Value {value} not found in the list.")

    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                print(f"Value {value} found at index {index}.")
                return True
            current = current.next
            index += 1
        print(f"Value {value} not found in the list.")
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("None")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beg(10)
    dll.insert_at_beg(11)
    dll.insert_at_end(20)
    dll.insert_at_end(22)
    dll.random_insert(30, 2)
    dll.display()  

    dll.delete_at_beg()  
    dll.display()  

    dll.delete_at_end()  
    dll.display()  

    dll.delete_by_value(30)  
    dll.display()  

    dll.search(20)  
    dll.search(100)  
  