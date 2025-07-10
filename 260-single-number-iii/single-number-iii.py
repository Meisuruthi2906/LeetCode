class Solution:
    def singleNumber(self, nums):
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        diff_bit = xor_sum & (-xor_sum)
        num1 = 0
        num2 = 0
        for num in nums:
            if (num & diff_bit) != 0:  
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]