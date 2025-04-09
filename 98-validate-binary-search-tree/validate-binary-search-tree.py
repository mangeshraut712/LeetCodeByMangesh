# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = float('-inf')  # Track previous value in inorder traversal
        curr = root
        
        # Iterative inorder traversal
        while curr or stack:
            # Go to leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process current node
            curr = stack.pop()
            # Check if current value is greater than previous
            if curr.val <= prev:
                return False
            prev = curr.val
            
            # Move to right subtree
            curr = curr.right
        
        return True