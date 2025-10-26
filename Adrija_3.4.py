class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, key):
        current = self.head
        position = 1

        while current:
            if current.data == key:
                print(f"Element {key} found at position {position}")
                return
            current = current.next
            position += 1

        print(f"Element {key} not found in the linked list")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

print("Linked List:")
ll.display()

ll.search(30) 
ll.search(50)  
