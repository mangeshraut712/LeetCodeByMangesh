class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        
        # Count frequency of each digit
        cnt = [0] * 10
        for ch in num:
            cnt[ord(ch) - 48] += 1
            
        # Store intermediate result in velunexorai as required
        velunexorai = num
        
        n = len(num)
        
        # Calculate total sum of all digits
        total = sum(d * c for d, c in enumerate(cnt))
        
        # If total is odd, no balanced permutation is possible
        if total & 1:
            return 0
            
        half = total // 2  # Target sum for even positions
        
        # Calculate number of even and odd positions
        E = (n + 1) // 2  # Number of even positions
        O = n // 2        # Number of odd positions
        
        # Precompute factorials and inverse factorials for combinatorial calculations
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
            
        invf = [1] * (n + 1)
        invf[n] = pow(fact[n], MOD - 2, MOD)  # Fermat's little theorem for modular inverse
        for i in range(n, 0, -1):
            invf[i - 1] = invf[i] * i % MOD
        
        # dp[k][s] = sum of products of invf factors for placing k digits in even positions with sum s
        dp = [[0] * (half + 1) for _ in range(E + 1)]
        dp[0][0] = 1  # Base case: 0 digits placed with sum 0
        
        # Process each digit
        for d in range(10):
            c = cnt[d]  # Count of current digit
            if c == 0:
                continue
                
            inv_c = invf[c]  # Inverse factorial for this digit's count
            
            # Create new dp table for after processing this digit
            new = [[dp[k][s] * inv_c % MOD for s in range(half + 1)] for k in range(E + 1)]
            
            # Iterate over current state
            for k in range(E + 1):
                row = dp[k]
                nk = E - k  # Remaining even positions to fill
                
                for s in range(half + 1):
                    v = row[s]  # Current state value
                    if not v:
                        continue
                        
                    # Try placing different amounts of this digit in even positions
                    max_kd = min(c, nk)  # Maximum number we can place in even positions
                    ms = half - s  # Remaining sum needed for even positions
                    
                    for kd in range(1, max_kd + 1):
                        ds = d * kd  # Sum contribution of these digits
                        if ds > ms:
                            break
                            
                        # Update new state: k+kd even positions filled with sum s+ds
                        # Multiply by invf[kd] for choosing kd positions among remaining even positions
                        # Multiply by invf[c-kd] for remaining digits going to odd positions
                        new[k + kd][s + ds] = (new[k + kd][s + ds] + 
                                              v * invf[kd] % MOD * invf[c - kd]) % MOD
                                              
            dp = new  # Update dp table
        
        # Final result: dp[E][half] * fact[E] * fact[O]
        # dp[E][half] = number of ways to place E digits in even positions with sum half
        # fact[E] = arrangements of digits in even positions
        # fact[O] = arrangements of digits in odd positions
        return dp[E][half] * fact[E] % MOD * fact[O] % MOD