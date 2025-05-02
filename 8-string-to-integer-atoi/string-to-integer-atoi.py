class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2 ** 31 -1
        INT_MIN = -2 ** 31
        n = len(s)
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and s[i] == '+':
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1
        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        if res < INT_MIN:
            return INT_MIN
        elif res > INT_MAX:
            return INT_MAX

        return res