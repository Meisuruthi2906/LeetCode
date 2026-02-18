class Solution(object):
    def getSneakyNumbers(self, nums):
        nums.sort()
        result=[]
        count=0
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                result.append(nums[i])
                count+=1
                if count==2:
                    return result
        