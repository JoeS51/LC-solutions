class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        @cache
        def dfs(pos, curr_time, m, n):
            nonlocal waitCost
            x, y = pos
            if x < 0 or y < 0 or y >= m or x >= n:
                return float('inf')
            curr_cost = 0
                # curr_time += waitCost[y][x]
            curr_cost += (x + 1) * (y + 1)
            if x == n-1 and y == m-1:
                return curr_cost
            if curr_time != 0:
                curr_cost += waitCost[y][x]
                
            down = curr_cost + dfs((x, y+1), curr_time+1, m, n)
            right = curr_cost + dfs((x+1, y), curr_time+1, m, n)
            return min(down, right)
        
        return dfs((0, 0), 0, m, n)
        

