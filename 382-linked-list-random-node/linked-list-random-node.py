import random

class Solution:
    def __init__(self, head):
        self.a = []
        while head:
            self.a.append(head.val)
            head = head.next
        self.c = random.choice

    def getRandom(self) -> int:
        return self.c(self.a)
