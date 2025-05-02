from typing import List
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        Finds the maximum difference between successive elements in the sorted form of an array
        using a bucket sort approach for linear time and space complexity.

        Args:
            nums: An integer array.

        Returns:
            The maximum difference between successive elements in sorted form, or 0 if the array
            contains less than two elements.
        """
        n = len(nums)
        if n < 2:
            return 0

        # Find the minimum and maximum values in the array
        min_val = min(nums)
        max_val = max(nums)

        # If all elements are the same, the maximum gap is 0
        if min_val == max_val:
            return 0

        # Calculate the minimum possible gap between elements if they were evenly distributed.
        # This value determines the minimum size of each bucket.
        # We use max(1, ...) to ensure bucket_size is at least 1, preventing division by zero
        # and handling cases where (max_val - min_val) < (n - 1).
        bucket_size = max(1, (max_val - min_val) // (n - 1))

        # Calculate the number of buckets needed.
        # The range [min_val, max_val] is divided into segments of size bucket_size.
        # We add 1 to include the last bucket.
        num_buckets = (max_val - min_val) // bucket_size + 1

        # Create buckets to store the minimum and maximum values in each range.
        # Initialize each bucket with infinity for min and negative infinity for max.
        buckets = [(float('inf'), float('-inf')) for _ in range(num_buckets)]

        # Distribute numbers into buckets and update min/max for each bucket
        for num in nums:
            # Calculate the index of the bucket for the current number
            bucket_idx = (num - min_val) // bucket_size

            # Update the minimum and maximum values in the corresponding bucket
            buckets[bucket_idx] = (min(buckets[bucket_idx][0], num), max(buckets[bucket_idx][1], num))

        # Calculate the maximum gap by iterating through the buckets
        max_gap = 0
        # Keep track of the maximum value in the previous non-empty bucket
        prev_max = min_val

        # Iterate through the buckets
        for bucket_min, bucket_max in buckets:
            # Skip empty buckets (where min is still infinity)
            if bucket_min == float('inf'):
                continue

            # The maximum gap will occur between the maximum value of the previous
            # non-empty bucket and the minimum value of the current non-empty bucket.
            max_gap = max(max_gap, bucket_min - prev_max)

            # Update the previous maximum to the maximum of the current bucket
            prev_max = bucket_max

        return max_gap
