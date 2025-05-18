class NumArray:
    def __init__(self, nums):
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]
    def sumRange(self, left, right):
        return self.prefix_sums[right + 1] - self.prefix_sums[left]