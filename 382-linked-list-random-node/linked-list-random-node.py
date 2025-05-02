import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        ans = 0
        i = 1
        while node:
            if random.randrange(i) == 0:
                ans = node.val
            node = node.next
            i += 1
        return ans
