import sys
from math import log2
from math import comb

class Solution:
    MOD = 10**9 + 7

    def idealArrays(self, n: int, maxValue: int) -> int:
        # Sieve of Eratosthenes to find the smallest prime divisor for each number up to maxValue.
        # This is used for efficient prime factorization.
        mind = [0] * (maxValue + 1)
        for p in range(2, maxValue + 1):
            if mind[p] == 0: # If p is prime
                for i in range(p, maxValue + 1, p):
                    if mind[i] == 0: # If mind[i] is not set yet, set it to the smallest prime factor p
                        mind[i] = p

        # Precompute binomial coefficients C(n + k - 1, k) modulo MOD.
        # C(n + k - 1, k) represents the number of ways to distribute k identical items into n distinct bins.
        # In this problem, it counts the number of ways to distribute k factors of a prime
        # across the n positions in the ideal array's factorization.
        # The maximum exponent of any prime in maxValue determines the necessary size of this precomputation.
        # log2(maxValue) gives an upper bound on the maximum exponent.
        maxPow = int(log2(maxValue)) + 1
        C = [1] * (maxPow + 1)
        for i in range(1, maxPow + 1):
            # C(n + i - 1, i) = (n + i - 1)! / (i! * (n - 1)!)
            # We compute this iteratively and modulo MOD
            # C(N, k) = C(N, k-1) * (N - k + 1) / k
            # C(n + i - 1, i) = C(n + i - 2, i - 1) * (n + i - 1) / i
            # Using modular inverse for division
            C[i] = (C[i-1] * (n + i - 1) * pow(i, self.MOD - 2, self.MOD)) % self.MOD


        # The total number of ideal arrays is the sum over all possible values V for the last element (arr[n-1]).
        # For a fixed V, the number of ideal arrays ending with V is the number of ways to factor V
        # into n ordered factors (a_0, b_1, ..., b_{n-1} where V = a_0 * b_1 * ... * b_{n-1}).
        # If V = p1^e1 * p2^e2 * ..., the number of ways to factor V into n ordered factors is
        # C(e1 + n - 1, n - 1) * C(e2 + n - 1, n - 1) * ...
        # This is equivalent to distributing the e_j factors of each prime p_j into n bins.
        ans = 0
        for i in range(1, maxValue + 1): # Iterate through all possible values for the last element
            x = i
            prod = 1 # This will store the product of C terms for the prime factorization of i
            while x > 1:
                p = mind[x] # Smallest prime factor of x
                exp = 0 # Exponent of prime p in the factorization of x
                while x % p == 0:
                    x //= p
                    exp += 1
                # Multiply the product by C(n + exp - 1, exp) modulo MOD
                prod = (prod * C[exp]) % self.MOD

            # Add the number of ideal arrays ending with value i to the total count
            ans = (ans + prod) % self.MOD

        return ans
