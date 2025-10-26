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

    def detect_and_remove_loop(self):
        slow = self.head
        fast = self.head

        # Detect loop
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                self.remove_loop(slow)
                print("Loop removed from the linked list")
                return True

        print("No loop found in the linked list")
        return False

    def remove_loop(self, loop_node):
        ptr1 = self.head
        ptr2 = loop_node
        while ptr1.next != ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = None

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

ll.head.next.next.next.next = ll.head.next

ll.detect_and_remove_loop()

print("Linked list after removing loop:")
ll.display()
