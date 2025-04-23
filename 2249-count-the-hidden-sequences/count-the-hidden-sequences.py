from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        current_prefix_sum = 0
        min_prefix_sum = 0
        max_prefix_sum = 0

        for diff in differences:
            current_prefix_sum += diff
            min_prefix_sum = min(min_prefix_sum, current_prefix_sum)
            max_prefix_sum = max(max_prefix_sum, current_prefix_sum)

        range_of_prefix_sums = max_prefix_sum - min_prefix_sum

        possible_starts = (upper - lower) - range_of_prefix_sums + 1

        return max(0, possible_starts)