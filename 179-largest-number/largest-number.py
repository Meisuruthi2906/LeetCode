class Solution(object):
    def largestNumber(self, nums):
         nums = [str(v) for v in nums]
         nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
         return "0" if nums[0] == "0" else "".join(nums)