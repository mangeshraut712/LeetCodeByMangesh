import random
from collections import defaultdict

class Solution:
    def __init__(self, nums):
        d = defaultdict(list)
        for i, x in enumerate(nums): d[x].append(i)
        self.d = d

    def pick(self, target):
        return random.choice(self.d[target])
