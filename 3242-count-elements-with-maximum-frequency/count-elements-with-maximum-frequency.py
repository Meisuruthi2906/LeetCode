class Solution(object):
    def maxFrequencyElements(self, nums):
        count = collections.Counter(nums)
        maxFreq = max(count.values())
        return sum(freq == maxFreq for freq in count.values()) * maxFreq
        
        