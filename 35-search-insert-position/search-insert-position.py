class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for index, value in enumerate(nums):
            if value >= target:
                return index
        return len(nums)