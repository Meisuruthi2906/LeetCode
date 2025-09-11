class Solution(object):
    def sortVowels(self, s):
        VOWELS='aeiouAEIOU'
        ans=[]
        vowels=sorted([c for c in s if c in VOWELS])
        i=0
        for c in s:
            if c in VOWELS:
                ans.append(vowels[i])
                i+=1
            else:
                ans.append(c)
        return ''.join(ans)

        