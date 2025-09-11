class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return false
        s_to_t={}
        t_to_s={}
        for ch1,ch2 in zip(s,t):
            if(ch1 in s_to_t and s_to_t[ch1]!=ch2) or\
              (ch2 in t_to_s and t_to_s[ch2]!=ch1):
              return False
            s_to_t[ch1]=ch2
            t_to_s[ch2]=ch1
        return True
                