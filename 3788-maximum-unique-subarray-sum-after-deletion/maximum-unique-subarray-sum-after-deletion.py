class Solution(object):
    def maxSum(self, nums):
        mx = max(nums)
        if mx <= 0:
            return mx
        seen = set()
        total = 0
        for x in nums:
            if x > 0 and x not in seen:
                total += x
                seen.add(x)
        return total
