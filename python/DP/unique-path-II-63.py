class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    print(dp)
                    dp[i][j] = dp[i][j-1]
                    continue
                if j == 0:
                    dp[i][j] = dp[i-1][j]
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

# runtime: O(n)
# spacetime: O(n^2)
