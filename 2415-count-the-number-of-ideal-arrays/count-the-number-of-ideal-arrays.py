import math

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7
        mv = maxValue
        mind = list(range(mv+1))
        mind[0] = mind[1] = 1
        r = int(mv**0.5)
        for i in range(2, r+1):
            if mind[i] == i:
                for j in range(i*i, mv+1, i):
                    if mind[j] == j:
                        mind[j] = i
        L = mv.bit_length()
        inv = [1] * (L+1)
        for i in range(2, L+1):
            inv[i] = mod - (mod//i) * inv[mod % i] % mod
        C = [1] * (L+1)
        for k in range(1, L+1):
            C[k] = C[k-1] * (n+k-1) % mod * inv[k] % mod
        ans = 0
        for v in range(1, mv+1):
            x = v
            res = 1
            while x > 1:
                p = mind[x]; e = 0
                while x % p == 0:
                    x //= p; e += 1
                res = res * C[e] % mod
            ans += res
            if ans >= mod: ans -= mod
        return ans
