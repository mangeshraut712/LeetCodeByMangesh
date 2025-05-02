import random

class Solution:
    def __init__(self, nums):
        d = {}
        for i, x in enumerate(nums):
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]
        self.d = d
        self.rr = random.randrange

    def pick(self, t):
        lst = self.d[t]
        return lst[self.rr(len(lst))]
