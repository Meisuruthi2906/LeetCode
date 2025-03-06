class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        k=[]
        for i in set(arr):
            k.append(arr.count(i))
        if len(k)==len(set(k)):
           return True
        else:
           return False        