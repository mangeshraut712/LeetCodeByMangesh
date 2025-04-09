import collections
from typing import Optional, List

# Definition for a binary tree node (as provided by LeetCode context)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level order traversal of a binary tree using BFS.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of lists, where each inner list contains the node values
            at that level, from left to right.
        """
        # Initialize the result list
        levels = []
        
        # Handle the edge case of an empty tree
        if not root:
            return levels

        # Initialize a queue for BFS. Using deque for efficient appends and pops.
        queue = collections.deque([root])

        # Loop while there are nodes to process
        while queue:
            # Get the number of nodes at the current level
            level_length = len(queue)
            # Initialize a list to store node values for the current level
            current_level_values = []

            # Process all nodes currently in the queue (i.e., all nodes at the current level)
            for _ in range(level_length):
                # Dequeue the next node
                node = queue.popleft()
                # Add its value to the current level's list
                current_level_values.append(node.val)

                # Enqueue children for the next level, if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the completed level's values to the overall result list
            levels.append(current_level_values)

        # Return the list of levels
        return levels
