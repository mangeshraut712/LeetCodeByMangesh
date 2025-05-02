import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Initializes the object with the head of the singly-linked list.
    Provides a method to return a random node's value with equal probability.
    """
    def __init__(self, head: Optional[ListNode]):
        """
        Stores the head of the linked list.

        Args:
            head: The head node of the singly-linked list.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Chooses a node randomly from the list and returns its value.
        All nodes have an equal probability of being chosen.
        Uses Reservoir Sampling to handle potentially large linked lists
        without storing all node values.

        Returns:
            The value of a randomly selected node.
        """
        random_value = 0  # Initialize with a default value (will be overwritten)
        current_node = self.head
        count = 0  # Counter for the number of nodes visited

        # Iterate through the linked list using Reservoir Sampling
        while current_node:
            count += 1  # Increment the node count

            # With probability 1/count, decide to keep the current node's value
            # as the potential random value.
            # random.randint(1, count) generates an integer from 1 to count (inclusive).
            # If it's 1, we select the current node.
            if random.randint(1, count) == 1:
                random_value = current_node.val

            # Move to the next node
            current_node = current_node.next

        # After iterating through the entire list, random_value holds the value
        # of a randomly selected node with equal probability.
        return random_value


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
