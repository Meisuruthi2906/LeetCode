class Solution(object):
    def tribonacci(self, n):
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            a,b,c = 0,1,1
            for x in range(3,n+1):
                next_value=a+b+c
                a,b,c=b,c,next_value
            return c
        