class Solution(object):
    def findEvenNumbers(self, digits):
        ans = []
        count = collections.Counter(digits)
        for a in range(1, 10):
            for b in range(0, 10):
                for c in range(0, 9, 2):
                    if count[a] > 0 and count[b] > (
                        b == a) and count[c] > (
                            c == a) + (
                                c == b):
                      ans.append(a * 100 + b * 10 + c)
        return ans
        