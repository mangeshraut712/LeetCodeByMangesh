from typing import List
from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = 'L' + dominoes + 'R'
        n = len(s)
        res = list(s)

        left = 0
        for right in range(1, n):
            if s[right] == '.':
                continue

            if s[left] == s[right]:
                for k in range(left + 1, right):
                    res[k] = s[left]
            elif s[left] == 'R' and s[right] == 'L':
                l, r = left + 1, right - 1
                while l < r:
                    res[l] = 'R'
                    res[r] = 'L'
                    l += 1
                    r -= 1

            left = right

        return ''.join(res[1:-1])
