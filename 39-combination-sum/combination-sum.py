class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()  # Sorting helps in pruning
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])  # Append a copy of the current path
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # Since candidates are sorted, further elements will be larger
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  # Reuse same element
                path.pop()  # Backtrack
        
        backtrack(0, [], target)
        return res
        