class Solution(object):
    def minSplitMerge(self, nums1, nums2):
        from collections import deque

        start = nums1[:]
        target = nums2[:]
        if start == target:
            return 0

        q = deque([start])
        visited = {str(start): 0}

        while q:
            cur = q.popleft()
            steps = visited[str(cur)]
            n = len(cur)

            for L in range(n):
                for R in range(L, n):
                    sub = cur[L:R+1]
                    remain = cur[:L] + cur[R+1:]

                    for pos in range(len(remain)+1):
                        newArr = remain[:pos] + sub + remain[pos:]
                        key = str(newArr)
                        if key not in visited:
                            visited[key] = steps + 1
                            if newArr == target:
                                return steps + 1
                            q.append(newArr)
        return -1