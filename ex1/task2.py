class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sort(head):
    if head is None or head.next is None:
        return head

    mid = find_middle(head)
    left_half = head
    right_half = mid.next
    mid.next = None

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def find_middle(head):
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left is not None and right is not None:
        if left.value < right.value:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next

        current = current.next

    if left is not None:
        current.next = left
    elif right is not None:
        current.next = right

    return dummy.next

head = ListNode(3, ListNode(1, ListNode(4, ListNode(2, ListNode(5)))))

print("Initial list:")
current_node = head
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

head = merge_sort(head)

print("\nSorted list:")
current_node = head
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")
