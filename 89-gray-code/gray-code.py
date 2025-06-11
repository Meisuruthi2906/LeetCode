class Solution(object):
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]
        