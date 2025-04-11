class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = 1 if x >= 0 else -1
        reversed_str = str(abs(x))[::-1]
        result = sign * int(reversed_str)
        
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result