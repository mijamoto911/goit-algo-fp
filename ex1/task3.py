class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

print("First Sorted list:")
current_node = list1
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

print("\nSecond Sorted list:")
current_node = list2
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

merged_list = merge_sorted_lists(list1, list2)

print("\nConcatenated Sorted list:")
current_node = merged_list
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")
