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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def add_two_lists(l1, l2):
    p1 = l1.head
    p2 = l2.head
    carry = 0
    result = LinkedList()

    while p1 or p2 or carry:
        val1 = p1.data if p1 else 0
        val2 = p2.data if p2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        result.insert_at_end(total % 10)

        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next

    return result

l1 = LinkedList()
l1.insert_at_end(2)
l1.insert_at_end(4)
l1.insert_at_end(3)  

l2 = LinkedList()
l2.insert_at_end(5)
l2.insert_at_end(6)
l2.insert_at_end(4)  

print("First number:")
l1.display()
print("Second number:")
l2.display()

result = add_two_lists(l1, l2)
print("Sum of numbers:")
result.display()
