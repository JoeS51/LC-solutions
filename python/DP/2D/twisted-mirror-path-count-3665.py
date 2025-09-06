class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[(0,0)] * n for _ in range(m)]
        dp[0][0] = (1, 0)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                   continue 
                curr_val = grid[i][j]
                above_val = 0
                if i != 0:
                    if grid[i-1][j] == 0:
                        above_val = dp[i-1][j][0]
                    else:
                        above_val = dp[i-1][j][1]
                left_val = 0
                if j != 0:
                    if grid[i][j-1] == 0:
                        left_val = dp[i][j-1][0]
                    else:
                        left_val = dp[i][j-1][0]
                if curr_val == 0:
                    dp[i][j] = (above_val + left_val, 0)
                else:
                    dp[i][j] = (above_val, left_val)
        return dp[m-1][n-1][0] % (pow(10, 9) + 7)
        

