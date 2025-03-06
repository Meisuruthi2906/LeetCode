class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
    
        ans=[]
        def palindrome(s):
            x=s[::-1]
            if x==s:
                return True
            return False
        for i in range(len(words)):
            if palindrome(words[i]) is True:
                ans.append(words[i])
        if len(ans)==0:
            return ""
        return ans[0]            

        