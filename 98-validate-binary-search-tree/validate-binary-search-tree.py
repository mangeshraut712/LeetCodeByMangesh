# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Check if current node's value is within the valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recurse: left subtree must be < node.val, right must be > node.val
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        
        return validate(root, float('-inf'), float('inf'))