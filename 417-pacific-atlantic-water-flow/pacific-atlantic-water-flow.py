class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]     
        def dfs(i, j, visited, prev_height):
            if (i < 0 or i >= m or j < 0 or j >= n or
                visited[i][j] or heights[i][j] < prev_height):
                return
            visited[i][j] = True
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dx, dy in directions:
                dfs(i + dx, j + dy, visited, heights[i][j])
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n - 1, atlantic, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m - 1, j, atlantic, heights[m - 1][j])
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])       
        return result
