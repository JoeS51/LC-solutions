class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        glob = 0
        mapid = {}
        mapsize = {}
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, m, n, id, count):
            nonlocal glob
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 2
                mapid[(i, j)] = id
                max_size = 0
                glob += 1  
                for x, y in dirs:
                    dfs(i + x, j + y, m, n, id, count)
                return count
            else:
                return 0

        id = 0
        ans = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = dfs(i, j, m, n, id, 0)
                    mapsize[id] = glob
                    ans = max(ans, glob)
                    glob = 0
                    id += 1
        print(ans)
        print(mapid)
        print(mapsize)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    up = -1
                    down = -1
                    right = -1
                    left = -1
                    if i > 0 and (i-1, j) in mapid:
                        up = mapid[(i-1, j)]
                        ans = max(ans, mapsize[up]+1)
                    if i < m - 1 and (i +1, j) in mapid:
                        down = mapid[(i+1, j)]
                        ans = max(ans, mapsize[down]+1)
                    if j > 0 and (i, j-1) in mapid:
                        left = mapid[(i, j-1)]
                        ans = max(ans, mapsize[left]+1)
                    if j < n - 1 and (i, j+1) in mapid:
                        right = mapid[(i, j+1)]
                        ans = max(ans, mapsize[right]+1)
                    lst = [up, down, left, right]
                    if (len(lst) == len(set(lst))) and up != -1 and left != -1 and right != -1 and down != -1:
                        ans = max(ans, mapsize[up] + mapsize[down] + mapsize[left] + mapsize[right] + 1)
                    if (up != right and up != left and left != right) and up != -1 and left != -1 and right != -1:
                        print("right")
                        ans = max(ans, mapsize[up] + mapsize[left] + mapsize[right] + 1)
                    if (left != right and left != down and down != right) and left != -1 and right != -1 and down != - 1:
                        print("up")
                        print(ans)
                        ans = max(ans, mapsize[down] + mapsize[left] + mapsize[right] + 1)
                        print(ans)
                    if (up != right and up != down and right != down) and up != -1 and right != -1 and down != -1:
                        print("down")
                        ans = max(ans, mapsize[up] + mapsize[down] + mapsize[right] + 1)
                    if (up != left and left != down and up != down) and up != -1 and left != -1 and down != -1:
                        print("last")
                        ans = max(ans, mapsize[up] + mapsize[left] + mapsize[down] + 1)

                    for x in [up, left, right, down]:
                        for y in [up, left, right, down]:
                            if x == y or x == -1 or y == -1:
                                continue
                            ans = max(ans, mapsize[x] + mapsize[y] + 1)

        return ans
        

                    
                

        
        

