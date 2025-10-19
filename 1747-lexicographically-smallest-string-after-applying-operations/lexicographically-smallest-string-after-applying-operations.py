from collections import deque
class Solution:
    def findLexSmallestString(self, s, a, b):
        n = len(s)
        ans = s     
        visited = set()
        q = deque([s])
        visited.add(s)
        while q:
            current_s = q.popleft()        
            if current_s < ans:
                ans = current_s     
            s_after_add = list(current_s)
            for i in range(1, n, 2): 
                s_after_add[i] = str((int(s_after_add[i]) + a) % 10)
            s_after_add = "".join(s_after_add)        
            if s_after_add not in visited:
                visited.add(s_after_add)
                q.append(s_after_add)
            s_after_rotate = current_s[n - b:] + current_s[:n - b]          
            if s_after_rotate not in visited:
                visited.add(s_after_rotate)
                q.append(s_after_rotate)             
        return ans
