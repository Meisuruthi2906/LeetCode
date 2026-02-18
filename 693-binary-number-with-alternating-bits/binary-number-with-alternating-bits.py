class Solution(object):
    def hasAlternatingBits(self, n):
        curr =n & 1
        n>>=1
        while n:
            prev =curr
            curr=n&1
            if curr==prev:
                return False

            n>>=1
        return True
        