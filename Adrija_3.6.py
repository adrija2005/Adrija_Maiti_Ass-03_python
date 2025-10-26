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

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Loop detected in the linked list")
                return True

        print("No loop found in the linked list")
        return False

    def display(self):
        current = self.head
        visited = set()
        while current:
            if current in visited:  
                print(f"{current.data} -> ... (loop starts here)")
                break
            print(current.data, end=" -> ")
            visited.add(current)
            current = current.next
        else:
            print("None")

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.head.next.next.next.next = ll.head.next

ll.detect_loop()
