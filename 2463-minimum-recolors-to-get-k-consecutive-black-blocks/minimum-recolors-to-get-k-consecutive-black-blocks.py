class Solution(object):
    def minimumRecolors(self, blocks, k):
        white=0
        for i in range(k):
            if blocks[i] == 'W':
                white +=1
        res=white

        for i in range(k,len(blocks)):
            if blocks[i] =='W':
                white +=1
            if blocks[i-k] == 'W':
                white -=1
            res = min(res,white)

        return res