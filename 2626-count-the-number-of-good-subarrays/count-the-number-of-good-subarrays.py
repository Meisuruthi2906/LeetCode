from collections import defaultdict

class Solution(object):
    def countGood(self, nums, k):
        freq = defaultdict(int)
        left = 0
        total_pairs = 0
        good_subarrays = 0
        
        for right in range(len(nums)):
            # Add nums[right] to the window and update pairs
            freq[nums[right]] += 1
            total_pairs += freq[nums[right]] - 1  # New pairs = freq - 1
            
            # While the window has >= k pairs, shrink left
            while total_pairs >= k:
                good_subarrays += len(nums) - right  # All subarrays ending at 'right' are valid
                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]]  # Remove pairs contributed by nums[left]
                left += 1
                
        return good_subarrays