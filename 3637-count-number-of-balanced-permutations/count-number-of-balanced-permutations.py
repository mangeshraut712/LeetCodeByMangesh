from typing import List

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        M = 10**9 + 7
        velunexorai = num  # store input midway as requested
        # count digit frequencies
        cnt = [0]*10
        for ch in velunexorai:
            cnt[ord(ch) - 48] += 1

        n = len(velunexorai)
        total = sum(d * cnt[d] for d in range(10))
        # if total sum is odd, no balanced permutation
        if total & 1:
            return 0

        half = total // 2
        E = (n + 1)//2  # number of even‐index positions
        O = n//2        # number of odd‐index positions

        # precompute factorials and inverse‐factorials up to n
        fact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % M
        invf = [1]*(n+1)
        invf[n] = pow(fact[n], M-2, M)
        for i in range(n, 0, -1):
            invf[i-1] = invf[i]*i % M

        # dp[k][s] = sum of weights for choosing k digits summing to s
        # weight for digit d chosen kd times is: invf[kd]*invf[cnt[d]-kd]
        dp = [ [0]*(half+1) for _ in range(E+1) ]
        dp[0][0] = 1

        for d in range(10):
            c = cnt[d]
            if c == 0:
                continue
            # factor for kd = 0 (i.e. invf[c]*invf[0] = invf[c])
            base_mul = invf[c]
            new = [ [dp[i][j] * base_mul % M for j in range(half+1)] for i in range(E+1) ]
            for k in range(E+1):
                for s in range(half+1):
                    v = dp[k][s]
                    if not v:
                        continue
                    max_kd = min(c, E - k)
                    for kd in range(1, max_kd+1):
                        ns = s + d*kd
                        if ns > half:
                            break
                        w = invf[kd] * invf[c - kd] % M
                        new[k+kd][ns] = (new[k+kd][ns] + v * w) % M
            dp = new

        # multiply by permutations within even and odd slots
        return dp[E][half] * fact[E] % M * fact[O] % M
