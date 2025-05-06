class Solution(object):
    def divide(self, dividend, divisor):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                if temp_divisor << 1 <= dividend:
                    temp_divisor <<= 1
                    multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        if negative:
            quotient = -quotient 
        return min(max(quotient, INT_MIN), INT_MAX)
        