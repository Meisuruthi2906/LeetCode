class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator // denominator)
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer_part = numerator // denominator
        result.append(str(integer_part))
        result.append(".")
        remainder = numerator % denominator
        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, "(")
                result.append(")")
                break
            remainder_map[remainder] = len(result)
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator
        return "".join(result)
