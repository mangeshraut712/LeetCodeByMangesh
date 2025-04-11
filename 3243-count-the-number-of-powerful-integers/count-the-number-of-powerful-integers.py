class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        s_len = len(s)
        s_val = int(s)
        if s_val > finish:
            return 0
        
        def solve(num_int):
            if num_int < s_val:
                return 0
            num_str = str(num_int)
            n = len(num_str)
            
            @lru_cache(None)
            def dp(idx: int, is_tight: bool, is_leading: bool) -> int:
                if idx == n:
                    return 1 if not is_leading else 0

                res = 0
                upper_bound = int(num_str[idx]) if is_tight else 9
                
                for digit in range(upper_bound + 1):
                    if digit > limit:
                        continue
                    if idx >= n - s_len and digit != int(s[idx - (n - s_len)]):
                        continue
                    current_is_leading = is_leading and (digit == 0)
                    new_tight = is_tight and (digit == upper_bound)
                    res += dp(idx + 1, new_tight, current_is_leading)

                return res

            return dp(0, True, True)

        return solve(finish) - solve(start - 1)