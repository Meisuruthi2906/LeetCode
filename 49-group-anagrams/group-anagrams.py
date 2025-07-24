import collections  
class Solution(object):
    def groupAnagrams(self, strs):
        dict = collections.defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word)) 
            dict[key].append(word)      
        return list(dict.values())

        
        