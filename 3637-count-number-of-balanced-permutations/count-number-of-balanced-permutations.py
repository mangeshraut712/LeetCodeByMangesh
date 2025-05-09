from typing import List

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        cnt = [0]*10
        for ch in num:
            cnt[ord(ch)-48] += 1
        n = len(num)
        total = sum(d*c for d,c in enumerate(cnt))
        if total & 1:
            return 0
        half = total // 2
        E = (n + 1)//2
        O = n//2

        # factorials and inverse factorials up to n
        fact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % MOD
        invf = [1]*(n+1)
        invf[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invf[i-1] = invf[i]*i % MOD

        # dp[k][s] = sum of products of invf factors for first digits
        dp = [[0]*(half+1) for _ in range(E+1)]
        dp[0][0] = 1

        for d in range(10):
            c = cnt[d]
            if c == 0:
                continue
            inv_c = invf[c]
            new = [[dp[k][s]*inv_c % MOD for s in range(half+1)] for k in range(E+1)]
            for k in range(E+1):
                row = dp[k]
                nk = E - k
                for s in range(half+1):
                    v = row[s]
                    if not v:
                        continue
                    max_kd = min(c, nk)
                    ms = half - s
                    for kd in range(1, max_kd+1):
                        ds = d*kd
                        if ds > ms:
                            break
                        new[k+kd][s+ds] = (new[k+kd][s+ds] +
                            v * invf[kd] % MOD * invf[c-kd]) % MOD
            dp = new

        return dp[E][half] * fact[E] % MOD * fact[O] % MOD
