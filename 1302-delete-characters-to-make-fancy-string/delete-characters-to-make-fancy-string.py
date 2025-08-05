class Solution(object):
    def makeFancyString(self, s):
        res = []
        count = 0
        prev = ''        
        for ch in s:
            if ch == prev:
                count += 1
            else:
                count = 1
            if count < 3:
                res.append(ch)
            prev = ch
        
        return "".join(res)
