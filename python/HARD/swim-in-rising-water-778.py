class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[inf] * m for _ in range(m)]
        dist[0][0] = inf
        q = [(grid[0][0], 0, 0)]
        while q:
            weight, i, j = heapq.heappop(q)
            if weight >= dist[i][j]:
                continue
            dist[i][j] = weight
            if i == n-1 and j == m-1:
                return weight
            if i > 0: # top cell
                # dist[i-1][j] = max(weight, grid[i-1][j])
                heapq.heappush(q, (max(weight, grid[i-1][j]), i-1, j))
            if j > 0: # left cell
                # dist[i][j-1] = max(weight, grid[i][j-1])
                heapq.heappush(q, (max(weight, grid[i][j-1]), i, j-1))
            if i < n-1: # bottom cell
                # dist[i+1][j] = max(weight, grid[i+1][j])
                heapq.heappush(q, (max(weight, grid[i+1][j]), i+1, j))
            if j < m-1: # right cell
                # dist[i][j+1] = max(weight, grid[i][j+1])
                heapq.heappush(q, (max(weight, grid[i][j+1]), i, j+1))
        return -1
        

