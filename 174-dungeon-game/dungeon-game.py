class Solution(object):
    def calculateMinimumHP(self, dungeon):
        n, m = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    next_min = 1
                elif i == n - 1:
                    next_min = dp[i][j + 1]
                elif j == m - 1:
                    next_min = dp[i + 1][j]
                else:
                    next_min = min(dp[i][j + 1], dp[i + 1][j])
                dp[i][j] = max(next_min - dungeon[i][j], 1)
        return dp[0][0]