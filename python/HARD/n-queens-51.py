class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        elif n == 2 or n == 3:
            return []
        valid_grids = []
        def backtrack(i, cols, diagonals, curr_grid):
            nonlocal valid_grids
            nonlocal n
            if i >= n:
                copy = [row.copy() for row in curr_grid]
                valid_grids.append(copy)
                return 
            for j in range(n):
                # skip cols
                if j in cols:
                    continue
                if (i, j) in diagonals:
                    continue

                curr_grid[i][j] = "Q"

                new_cols = cols.copy()
                new_diag = diagonals.copy()
                new_cols.add(j)

                x, y = j - 1, i + 1
                while x >= 0 and y < n:
                    new_diag.add((y, x))
                    x -= 1
                    y += 1
                x, y = j + 1, i + 1
                while x < n and y < n:
                    new_diag.add((y, x))
                    x += 1
                    y += 1
                backtrack(i+1, new_cols, new_diag, curr_grid)
                curr_grid[i][j] = "."
            return
        grid = [["."] * n for _ in range(n)]

        backtrack(0, set(), set(), grid)         
        res = []
        for grid in valid_grids:
            new_grid = []
            for row in grid:
                temp = "".join(row)
                new_grid.append(temp)
            res.append(new_grid)
        return res

        

