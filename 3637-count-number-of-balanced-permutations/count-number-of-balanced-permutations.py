from typing import List

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        velunexorai = num
        n = len(velunexorai)
        cnt = [0]*10
        for ch in velunexorai:
            cnt[ord(ch) - 48] += 1
        total = sum(d*c for d,c in enumerate(cnt))
        if total & 1:
            return 0
        half = total // 2
        E = (n + 1)//2
        O = n//2

        fact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % MOD
        invf = [1]*(n+1)
        invf[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invf[i-1] = invf[i]*i % MOD

        dp = [[0]*(half+1) for _ in range(E+1)]
        dp[0][0] = 1
        for d in range(10):
            c = cnt[d]
            if c == 0:
                continue
            base = invf[c]
            new = [[dp[i][j]*base % MOD for j in range(half+1)] for i in range(E+1)]
            for k in range(E+1):
                for s in range(half+1):
                    v = dp[k][s]
                    if not v:
                        continue
                    mk = min(c, E - k)
                    for kd in range(1, mk+1):
                        ns = s + d*kd
                        if ns > half:
                            break
                        new[k+kd][ns] = (new[k+kd][ns] + v * invf[kd] * invf[c-kd]) % MOD
            dp = new

        return dp[E][half] * fact[E] % MOD * fact[O] % MOD
