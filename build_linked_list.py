class TreeNode:
    def __init__(self,value = 0, next = None):
        self.val = value
        self.next = next


def build_linked_list(arr:list):
    root = TreeNode(arr[0])
    curr = root
    for num in arr[1:]:
        curr.next = TreeNode(num)
        curr = curr.next
    return root

def print_linked_list(head:TreeNode):
    while head:
        print(head.val,end = "->" if head.next else "\n")
        head = head.next

def reverse_linked_list(head:TreeNode):
    prev = None
    curr = head
    
    while curr:
        next_head = curr.next
        curr.next = prev
        prev = curr
        curr = next_head
    return prev



array = [3,5,6,8,0,9]
root = build_linked_list(array)
print_linked_list(root)
reversed_list = reverse_linked_list(root)
print_linked_list(reversed_list)
