class Solution(object):
    def getNoZeroIntegers(self, n):
        def has_zero(x):
            while x>0:
                if x%10==0:
                    return True
                x//=10
            return False
        for a in range(1,n):
            b=n-a
            if not has_zero(a) and not has_zero(b):
                return[a,b]
        return[]

        