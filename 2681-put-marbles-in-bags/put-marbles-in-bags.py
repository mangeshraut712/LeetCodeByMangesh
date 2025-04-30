from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        if k == 1:
            return 0

        adjacent_sums = []
        for i in range(n - 1):
            adjacent_sums.append(weights[i] + weights[i+1])

        adjacent_sums.sort()

        min_sum_cuts = sum(adjacent_sums[:k-1])
        max_sum_cuts = sum(adjacent_sums[-(k-1):])

        return max_sum_cuts - min_sum_cuts
