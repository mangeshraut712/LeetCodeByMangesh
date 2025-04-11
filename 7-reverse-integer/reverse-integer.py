class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        sign = 1 if x >= 0 else -1
        abs_x = abs(x)
        reversed_num = 0
        
        while abs_x != 0:
            digit = abs_x % 10
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            reversed_num = reversed_num * 10 + digit
            abs_x //= 10
            
        result = sign * reversed_num
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result