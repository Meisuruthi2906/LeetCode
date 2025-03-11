class Solution(object):
    def numberOfSubstrings(self, s):       
        d={"a":-1, "b":-1, "c":-1}
        ans=0
        for i, c in enumerate(s):
            d[c]=i
            ans+=min(d["a"], d["b"], d["c"])+1
        return ans
        
        