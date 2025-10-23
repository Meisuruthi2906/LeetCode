class Solution:
    def hasSameDigits(self, s):
        nums = [int(ch) for ch in s]      
        while len(nums) > 2:
            nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]     
        return nums[0] == nums[1]

        