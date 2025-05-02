from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(i))
            freq[digit_sum] += 1

        max_freq = 0
        if freq: # Handle case where n=0, though constraints say n>=1
            max_freq = max(freq.values())

        count = 0
        for group_size in freq.values():
            if group_size == max_freq:
                count += 1

        return count
