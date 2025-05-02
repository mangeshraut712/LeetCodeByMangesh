from typing import List
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        # Calculate bucket size. Ensure it's at least 1.
        # The formula (hi - lo + n - 2) // (n - 1) is a way to calculate
        # the minimum possible gap + 1, ensuring at least one empty bucket
        # between elements from different original buckets.
        bucket_size = max(1, (max_val - min_val) // (n - 1))

        # Calculate the number of buckets needed
        num_buckets = (max_val - min_val) // bucket_size + 1

        # Initialize buckets to store min and max values
        # Use values outside the possible range to indicate empty buckets
        min_buckets = [float('inf')] * num_buckets
        max_buckets = [float('-inf')] * num_buckets

        # Distribute numbers into buckets
        for num in nums:
            # Calculate bucket index
            bucket_idx = (num - min_val) // bucket_size
            # Update min and max in the bucket
            min_buckets[bucket_idx] = min(min_buckets[bucket_idx], num)
            max_buckets[bucket_idx] = max(max_buckets[bucket_idx], num)

        # Calculate the maximum gap
        max_gap = 0
        # Keep track of the maximum value from the previous non-empty bucket
        prev_max = min_val

        # Iterate through buckets to find the maximum gap
        for i in range(num_buckets):
            # Skip empty buckets
            if min_buckets[i] == float('inf'):
                continue

            # The gap is between the min of the current bucket and the max of the previous
            max_gap = max(max_gap, min_buckets[i] - prev_max)
            # Update the previous max to the max of the current bucket
            prev_max = max_buckets[i]

        return max_gap
