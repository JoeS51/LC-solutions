class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)
        m = len(board)
        n = len(board[0])
        empty = []
        for i in range(m):
            for j in range(n):
                curr_num = board[i][j]
                if curr_num == ".":
                    empty.append((i, j))
                    continue
                curr_num = int(curr_num)
                curr_grid = (i // 3) + ((j // 3) * 3)
                rows[i].add(curr_num)
                cols[j].add(curr_num)
                grids[curr_grid].add(curr_num)
        def isValid(i, coord):
            row, col = coord
            curr_grid = (row // 3) + ((col // 3) * 3)
            if i in rows[row] or i in cols[col] or i in grids[curr_grid]:
                return False
            return True
            

        def backtrack(idx):
            if idx >= len(empty):
                return True
            coordinates = empty[idx]
            row, col = coordinates
            for i in range(1, 10):
                if isValid(i, coordinates):
                    board[row][col] = str(i)
                    rows[row].add(i)
                    cols[col].add(i)
                    curr_grid = (row // 3) + ((col // 3) * 3)
                    grids[curr_grid].add(i)
                    if backtrack(idx+1):
                        return True
                    else:
                        board[row][col] = "."
                        rows[row].remove(i)
                        cols[col].remove(i)
                        grids[curr_grid].remove(i)
                else:
                    continue
            return False
        
        backtrack(0)

        

# time complexity: O(9^E)
# space complexity: O(E) just the empty list
