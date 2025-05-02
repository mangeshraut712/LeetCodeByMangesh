from typing import List

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        length = 0

        # Count all the '0's first, as they contribute to length but not value
        for char in s:
            if char == '0':
                length += 1

        current_value = 0
        bit_position = 0

        # Iterate from right to left to add '1's greedily
        # '1's at lower bit positions contribute less to the value
        for i in range(n - 1, -1, -1):
            # If the current character is '1'
            if s[i] == '1':
                # Calculate the potential value added by this '1' at its position
                # We only need to consider bit positions where 2^bit_position <= k.
                # Since k <= 10^9, 2^30 is approximately 10^9, so bit_position >= 30
                # will result in 2^bit_position > k.
                if bit_position < 31:
                    potential_add = 1 << bit_position

                    # If adding this '1' does not exceed k
                    if current_value + potential_add <= k:
                        current_value += potential_add
                        length += 1
                    # If adding this '1' exceeds k, we cannot add this '1' or any '1's to the left.
                    # We've already included all possible '0's.
                    # The loop will continue to increment bit_position, but the condition
                    # `current_value + (1 << bit_position) <= k` will remain false for subsequent '1's.
                    # So, no explicit break is needed here.

            # Increment the bit position for the next digit to the left
            bit_position += 1

        # The total length is the count of all '0's plus the '1's that could be added
        return length
