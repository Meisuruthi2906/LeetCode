class Solution(object):
    def myAtoi(self, s):
        s = s.strip()  
        if not s:
            return 0
        sign = 1
        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            s = s[1:]  
        num = 0
        for ch in s:
            if not ch.isdigit():
                break
            num = num * 10 + int(ch)
        num *= sign
        num = max(min(num, 2**31 - 1), -2**31)
        return num