class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxA = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            maxA = max(area, maxA)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxA 
        
        