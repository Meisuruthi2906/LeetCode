class Solution(object):
    def isTrionic(self, nums):
        if len(nums) < 4 : return False 
        inc = 0 
        x,y= 0,0
        c = 0
        for i in range(1,len(nums)) : 
            if nums[i] == nums[i-1] : return False
            if nums[i]<nums[i-1] and inc == 0 : 
                x = i-1
                inc = 1
                c+=1
            elif nums[i]>nums[i-1] and inc == 1 : 
                y = i-1
                inc = 0
                c+=1 
        return x<y and x!=0 and c==2





        
        