class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True
        
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s_char = s[i - 1]
                p_char = p[j - 1]
                
                if p_char == '.' or p_char == s_char:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p_char == '*':
                    # '*' matches zero preceding element
                    zero_match = dp[i][j - 2] 
                    
                    # '*' matches one or more preceding element
                    one_or_more_match = False
                    preceding_char = p[j - 2]
                    if preceding_char == '.' or preceding_char == s_char:
                        one_or_more_match = dp[i - 1][j]
                        
                    dp[i][j] = zero_match or one_or_more_match
                else:
                    # Character mismatch
                    dp[i][j] = False
                    
        return dp[m][n]