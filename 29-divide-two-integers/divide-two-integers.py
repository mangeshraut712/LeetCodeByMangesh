class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        is_negative = (dividend < 0) != (divisor < 0)

        neg_dividend = -abs(dividend)
        neg_divisor = -abs(divisor)

        quotient = 0

        while neg_dividend <= neg_divisor:
            temp_divisor = neg_divisor
            multiple = 1
            while neg_dividend <= (temp_divisor << 1) and (temp_divisor << 1) < 0:
                temp_divisor <<= 1
                multiple <<= 1

            neg_dividend -= temp_divisor
            quotient += multiple

        if is_negative:
            quotient = -quotient

        if quotient > INT_MAX:
            return INT_MAX
        if quotient < INT_MIN:
            return INT_MIN

        return quotient