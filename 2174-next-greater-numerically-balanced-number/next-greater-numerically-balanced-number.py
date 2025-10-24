class Solution:
    def nextBeautifulNumber(self, n):
        q = [1,22,122,333,1333,4444,14444,22333,55555,122333,155555,224444,666666,1224444]
        return next(v for v in sorted(int(''.join(p)) for s in map(str,q)
            for p in permutations(s)) if v>n)