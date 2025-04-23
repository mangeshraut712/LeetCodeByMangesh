from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Counts the number of groups with the largest size based on the sum of digits.

        Args:
            n: The upper limit of the integers to consider (from 1 to n).

        Returns:
            The number of groups that have the largest size.
        """
        def sum_digits(num):
            """
            Calculates the sum of the digits of a given integer.
            """
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        # Use a Counter to store the frequency of each digit sum
        group_counts = Counter()

        # Iterate through numbers from 1 to n
        for i in range(1, n + 1):
            digit_sum = sum_digits(i)
            group_counts[digit_sum] += 1

        # Find the maximum group size
        if not group_counts:
            return 0 # Should not happen based on constraints (n >= 1)
            
        max_group_size = 0
        for count in group_counts.values():
             max_group_size = max(max_group_size, count)

        # Count how many groups have the maximum size
        count_largest_groups = 0
        for count in group_counts.values():
            if count == max_group_size:
                count_largest_groups += 1

        return count_largest_groups