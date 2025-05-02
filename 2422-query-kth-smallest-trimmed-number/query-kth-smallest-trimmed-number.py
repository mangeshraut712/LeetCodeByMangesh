from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Assuming all strings have the same length based on constraints
        l = len(nums[0])
        answer = []

        # sorted_indices[t] will store the original indices of nums,
        # sorted based on their rightmost t+1 digits (0-indexed t).
        # This corresponds to trim = t + 1 in the queries.
        sorted_indices = [[] for _ in range(l)]

        # Initialize current_indices with the original indices
        current_indices = list(range(n))

        # Perform Radix Sort on the indices based on digits from right to left
        for p in range(l): # p is the digit position from the right (0-indexed)
            # The actual index of the digit in the string is l - 1 - p
            digit_index = l - 1 - p

            # Counting sort for the digit at position 'digit_index'
            counts = [0] * 10
            for original_idx in current_indices:
                digit = int(nums[original_idx][digit_index])
                counts[digit] += 1

            # Modify counts to store the actual position of each digit in the output array
            for i in range(1, 10):
                counts[i] += counts[i - 1]

            # Create an output array to store the sorted indices for this digit pass
            output_indices = [0] * n
            # Iterate through the current_indices in reverse order for stability
            for i in range(n - 1, -1, -1):
                original_idx = current_indices[i]
                digit = int(nums[original_idx][digit_index])
                # Calculate the position in the output array using the modified counts
                position = counts[digit] - 1
                # Place the original index in the output array
                output_indices[position] = original_idx
                # Decrement the count for this digit
                counts[digit] -= 1

            # Update current_indices with the sorted order for the next digit pass
            current_indices = output_indices

            # Store the sorted indices for the current 'trim' level (p + 1)
            # sorted_indices[p] corresponds to trimming to p + 1 digits
            sorted_indices[p] = current_indices[:] # Store a copy

        # Process each query
        for k, trim in queries:
            # The answer for a query [k, trim] is the (k-1)-th element
            # in the list of indices sorted by the rightmost 'trim' digits.
            # This corresponds to sorted_indices[trim - 1].
            answer.append(sorted_indices[trim - 1][k - 1])

        return answer
