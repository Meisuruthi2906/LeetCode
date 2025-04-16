from collections import defaultdict

class Solution(object):
    def countGood(self, nums, k):
        freq = defaultdict(int)
        left = 0
        total_pairs = 0
        good_subarrays = 0
        
        for right in range(len(nums)):
           
            freq[nums[right]] += 1
            total_pairs += freq[nums[right]] - 1  
            
            
            while total_pairs >= k:
                good_subarrays += len(nums) - right  
                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]] 
                left += 1
                
        return good_subarrays