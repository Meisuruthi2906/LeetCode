class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        c=0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    c+=1
                    baskets.pop(j)
                    break
        return len(fruits)-c