from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        answer = []

        for k, trim in queries:
            # Create a list of tuples (trimmed_number_string, original_index)
            # The trimmed number is the rightmost 'trim' digits.
            # We include the original index for stable sorting (tie-breaking).
            trimmed_indexed_nums = [(num[-trim:], i) for i, num in enumerate(nums)]

            # Sort the list of tuples. Python's sort is stable, so the original index
            # will correctly break ties if trimmed numbers are equal.
            trimmed_indexed_nums.sort()

            # The k-th smallest trimmed number is at index k-1 in the sorted list.
            # The answer is the original index of this element.
            answer.append(trimmed_indexed_nums[k - 1][1])

        return answer
