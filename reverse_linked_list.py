class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
# --- Helper Functions ---

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" → " if head.next else "\n")
        head = head.next

# --- Test Case ---

# Input: 1 → 2 → 3 → 4 → 5
head = build_linked_list([1, 2, 3, 4, 5])

print("Original List:")
print_linked_list(head)

sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed List:")
print_linked_list(reversed_head)
