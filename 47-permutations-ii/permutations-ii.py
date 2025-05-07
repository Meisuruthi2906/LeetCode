class Solution(object):
    def permuteUnique(self, nums):
        return list(map(list, set(permutations(nums))))