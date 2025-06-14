class Solution:
    def combine(self, n , k):
        combs = [[]]
        for _ in range(k):
            temp = []
            for c in combs:
                for i in range(1, c[0] if c else n+1):
                    temp.append([i]+c)
            combs = temp
        return combs