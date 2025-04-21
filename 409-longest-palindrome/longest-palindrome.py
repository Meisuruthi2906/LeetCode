class Solution(object):
    def longestPalindrome(self, s):
        d = set()
        for char in s:
            if char not in d:
                d.add(char)
            else:
                d.remove(char)
        if len(d) != 0:
            return len(s) - len(d) + 1
        else:
            return len(s)