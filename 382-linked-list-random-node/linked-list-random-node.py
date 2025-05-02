import random

class Solution:
    def __init__(self, head):
        self.h, self.rr = head, random.randrange

    def getRandom(self):
        node, ans, i = self.h, 0, 1
        while node:
            if self.rr(i) == 0:
                ans = node.val
            node = node.next
            i += 1
        return ans
