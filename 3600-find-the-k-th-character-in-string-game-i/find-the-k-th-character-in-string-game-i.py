class Solution:
    def kthCharacter(self, k):
        return chr(ord('a') + bin(k - 1).count('1'))