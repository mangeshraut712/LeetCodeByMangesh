import random
from typing import List
from collections import defaultdict

class Solution:
    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # Retrieve the list of indices for the target number
        target_indices = self.indices[target]
        # Randomly select an index from the list
        return random.choice(target_indices)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
