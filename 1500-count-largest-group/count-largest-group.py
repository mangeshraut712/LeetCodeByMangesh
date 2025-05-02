from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = Counter(sum(map(int, str(i))) for i in range(1, n+1))
        M = max(cnt.values())
        return sum(v == M for v in cnt.values())
