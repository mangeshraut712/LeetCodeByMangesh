class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        # The maximum exponent for any prime factor in a number up to maxValue (10^4)
        # is relatively small. For example, 2^13 = 8192, 2^14 = 16384. Max exponent is around 14.
        # We need combinations C(b + n - 1, n - 1). The maximum value for the upper part
        # is roughly max_exponent + n - 1.
        max_comb_n = n + 14 # A safe upper bound for b + n - 1

        # Precompute factorials and inverse factorials modulo MOD
        fact = [1] * (max_comb_n + 1)
        invFact = [1] * (max_comb_n + 1)
        for i in range(2, max_comb_n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            invFact[i] = pow(fact[i], MOD - 2, MOD) # Modular inverse using Fermat's Little Theorem

        def combinations(N, K):
            """Calculates N choose K modulo MOD."""
            if K < 0 or K > N:
                return 0
            if K == 0 or K == N:
                return 1
            if fact[K] == 0 or fact[N-K] == 0: # Should not happen with prime MOD
                 return 0
            return (fact[N] * invFact[K] % MOD * invFact[N - K] % MOD)

        total_ideal_arrays = 0

        # Iterate through all possible values for the last element of the ideal array
        for y in range(1, maxValue + 1):
            current_y = y
            prime_exponents = {}

            # Find the prime factorization of y
            d = 2
            while d * d <= current_y:
                while current_y % d == 0:
                    prime_exponents[d] = prime_exponents.get(d, 0) + 1
                    current_y //= d
                d += 1
            if current_y > 1:
                prime_exponents[current_y] = prime_exponents.get(current_y, 0) + 1

            # Calculate the number of ways to form an ideal array of length n ending with y
            # This is the product of C(b + n - 1, n - 1) for each prime factor with exponent b
            current_contribution = 1
            for b in prime_exponents.values():
                current_contribution = (current_contribution * combinations(b + n - 1, n - 1)) % MOD

            total_ideal_arrays = (total_ideal_arrays + current_contribution) % MOD

        return total_ideal_arrays