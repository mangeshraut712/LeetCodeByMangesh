from typing import List

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        value = 0
        length = 0

        for ch in reversed(s):
            if ch == '0':
                length += 1
            else:
                weight = 1 << length
                if value + weight <= k:
                    value += weight
                    length += 1

        return length
