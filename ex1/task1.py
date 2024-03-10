class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Initial list:")
current_node = head
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

head = reverse_linked_list(head)

print("\nReversed list:")
current_node = head
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

