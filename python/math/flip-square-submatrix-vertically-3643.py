class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        for i in range(0, k//2):
            for j in range(y, y+k):
                curr_val = grid[x+i][j]
                flip_val = grid[k+x-i-1][j]
                grid[x+i][j] = flip_val
                grid[k+x-i-1][j] = curr_val
        return grid
# runtime: O(N)
# spacetime: O(1)
