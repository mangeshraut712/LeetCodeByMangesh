class Solution:
    MOD = 10**9 + 7

    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = self.MOD
        # linear sieve for smallest prime factor
        mind = [0] * (maxValue + 1)
        primes = []
        for i in range(2, maxValue + 1):
            if mind[i] == 0:
                mind[i] = i
                primes.append(i)
            for p in primes:
                ip = i * p
                if ip > maxValue or p > mind[i]:
                    break
                mind[ip] = p

        # precompute inv[1..L] and C[k] = C(n+k-1, k)
        L = (maxValue.bit_length())
        inv = [1] * (L + 1)
        for i in range(2, L + 1):
            inv[i] = mod - (mod // i) * inv[mod % i] % mod
        C = [1] * (L + 1)
        for k in range(1, L + 1):
            C[k] = C[k - 1] * (n + k - 1) % mod * inv[k] % mod

        ans = 0
        for v in range(1, maxValue + 1):
            x = v
            res = 1
            while x > 1:
                p = mind[x]
                e = 0
                while x % p == 0:
                    x //= p
                    e += 1
                res = res * C[e] % mod
            ans += res
        return ans % mod
