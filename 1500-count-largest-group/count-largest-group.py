class Solution:
    def countLargestGroup(self, n: int) -> int:
        arr = [0] * 37
        for i in range(1, n + 1):
            x, s = i, 0
            while x:
                s += x % 10
                x //= 10
            arr[s] += 1
        M = 0
        cnt = 0
        for v in arr:
            if v > M:
                M = v
                cnt = 1
            elif v == M:
                cnt += 1
        return cnt
