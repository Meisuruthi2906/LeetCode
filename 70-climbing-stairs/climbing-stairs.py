class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n== 2:
            return 2
        else:
            x,y=1,2
            for i in range(3,n+1):
                x,y=y,x+y
            return y