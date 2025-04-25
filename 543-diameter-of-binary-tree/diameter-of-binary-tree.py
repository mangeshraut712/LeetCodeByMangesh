from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def height(node):
            nonlocal max_diameter

            if node is None:
                return -1

            left_height = height(node.left)
            right_height = height(node.right)

            current_diameter = left_height + right_height + 2
            max_diameter = max(max_diameter, current_diameter)

            return max(left_height, right_height) + 1

        height(root)
        return max_diameter