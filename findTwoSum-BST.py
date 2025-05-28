from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def inOrder(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return inOrder(node.left) or inOrder(node.right)
        
        return inOrder(root)

# Helper function to insert nodes into the binary search tree
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

# Build the test tree: [5, 3, 6, 2, 4, null, 7]
vals = [5, 3, 6, 2, 4, 7]
root = None
for v in vals:
    root = insert_into_bst(root, v)

# Run test
solution = Solution()
target = 9
print("Does a pair sum to", target, "?", solution.findTarget(root, target))  # Expected: True (2 + 7)
