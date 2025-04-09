# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Pass 1: Create copies and interweave them
        curr = head
        while curr:
            copied = Node(curr.val)
            copied.next = curr.next
            curr.next = copied
            curr = copied.next

        # Pass 2: Set random pointers for copied nodes
        curr = head
        while curr:
            copied = curr.next
            if curr.random:
                copied.random = curr.random.next # curr.random's copy
            curr = copied.next

        # Pass 3: Separate the lists
        dummy = Node(0) # Dummy head for the new list
        copied_curr = dummy
        curr = head
        while curr:
            # Extract copied node
            copied_node = curr.next # Get the copy
            copied_curr.next = copied_node # Link it to the new list
            copied_curr = copied_curr.next # Advance the new list tail

            # Restore original list
            curr.next = copied_node.next # Point original node to the next original
            
            # Advance original list pointer
            curr = curr.next 

        return dummy.next

# --- Complexity Analysis ---
# Time Complexity: O(N) - Three passes through the list.
# Space Complexity: O(1) - Constant extra space (excluding the output list itself).
