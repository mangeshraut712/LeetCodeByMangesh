import random
from collections import defaultdict

class Solution:
    def __init__(self, nums):
        self.d = defaultdict(list)
        for i, x in enumerate(nums):
            self.d[x].append(i)

    def pick(self, t):
        return random.choice(self.d[t])
