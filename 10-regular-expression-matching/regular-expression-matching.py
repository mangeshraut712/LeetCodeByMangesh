class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}
        
        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base cases
            if j == n:
                return i == m
            if i > m:
                return False
            
            # First characters match
            first_match = i < m and (p[j] == s[i] or p[j] == '.')
            
            if j + 1 < n and p[j + 1] == '*':
                # '*' can match zero or one/more
                result = (dp(i, j + 2) or  # Zero match
                         (first_match and dp(i + 1, j)))  # One or more match
            else:
                result = first_match and dp(i + 1, j + 1)
            
            memo[(i, j)] = result
            return result
        
        return dp(0, 0)