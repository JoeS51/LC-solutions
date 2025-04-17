class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, m, n):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 0
            dfs(grid, i-1, j, m, n)
            dfs(grid, i+1, j, m, n)
            dfs(grid, i, j-1, m, n)
            dfs(grid, i, j+1, m, n)

        m = len(grid) 
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                # on edgej
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n-1):
                    dfs(grid, i, j, m, n)
        count = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count
# runtime: O(m x n)
# spacetime: O(m x n)
