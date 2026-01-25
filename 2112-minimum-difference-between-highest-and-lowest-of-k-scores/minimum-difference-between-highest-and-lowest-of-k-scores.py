class Solution(object):
    def minimumDifference(self, nums, k):
        if k==1:
            return 0

        nums.sort()
        n=len(nums)
        ans=float('inf')
        for i in range(n-k+1):
            diff=nums[i+k-1]-nums[i]
            if diff < ans:
                ans = diff
        return ans
        
        