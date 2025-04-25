from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        current_prefix_sum_mod = 0
        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1

        for num in nums:
            current_prefix_sum_mod = (current_prefix_sum_mod + (1 if num % modulo == k else 0)) % modulo

            target_remainder = (current_prefix_sum_mod - k + modulo) % modulo

            count += remainder_counts[target_remainder]

            remainder_counts[current_prefix_sum_mod] += 1

        return count