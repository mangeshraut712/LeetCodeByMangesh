from typing import List

MOD = 10**9 + 7

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        cnt = [0]*10
        for ch in num:
            cnt[ord(ch)-48] += 1

        total = sum(d * cnt[d] for d in range(10))
        if total & 1:
            return 0
        half = total // 2
        E = (n + 1) // 2
        O = n // 2

        # precompute factorials and inv factorials up to n
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD
        invf = [1] * (n+1)
        invf[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invf[i-1] = invf[i] * i % MOD

        # dp[k][s] = ways (weighted) to choose k digits summing to s
        dp = [[0]*(half+1) for _ in range(E+1)]
        dp[0][0] = 1

        for d in range(10):
            c = cnt[d]
            if c == 0:
                continue
            new = [[0]*(half+1) for _ in range(E+1)]
            for k in range(E+1):
                for s in range(half+1):
                    v = dp[k][s]
                    if not v:
                        continue
                    max_kd = min(c, E-k)
                    for kd in range(max_kd+1):
                        ns = s + d*kd
                        if ns > half:
                            break
                        # weight = 1/(kd! * (c-kd)!)
                        w = invf[kd] * invf[c-kd] % MOD
                        new[k+kd][ns] = (new[k+kd][ns] + v * w) % MOD
            dp = new

        # multiply by permutations within even and odd slots
        return dp[E][half] * fact[E] % MOD * fact[O] % MOD
