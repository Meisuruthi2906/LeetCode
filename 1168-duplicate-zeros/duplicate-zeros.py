class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        m=0
        n=len(arr)-1
        while(m<n):
            if(arr[m]==0):
                arr.insert(m+1,0)
                arr.pop()
                m+=1
            m+=1