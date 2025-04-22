class Solution(object):
    def subsets(self, nums):
        subset=[[]]
        for i in nums:
            subset+=[[i]+ j for j in subset]
        return subset