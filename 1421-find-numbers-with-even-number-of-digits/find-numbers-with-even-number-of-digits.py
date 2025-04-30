from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Counts the number of integers in an array that have an even number of digits.

        Uses mathematical comparisons to determine the number of digits.

        Args:
            nums: A list of integers.

        Returns:
            The count of numbers with an even number of digits.
        """
        count = 0
        for num in nums:
            # Determine the number of digits using mathematical comparisons
            if 10 <= num <= 99:
                # 2 digits (even)
                count += 1
            elif 1000 <= num <= 9999:
                # 4 digits (even)
                count += 1
            elif num == 100000:
                # 6 digits (even)
                count += 1
            # Numbers with 1, 3, or 5 digits (1-9, 100-999, 10000-99999) are skipped

        return count

