"""
1. first look at all bombs and make all adjacents squares += 1
2. go to the click coordinate and perform BFS or DFS. if they click a bomb game over
    - if it is E then make it B and keep recursing
    - if it is M then keep it as M 
    - if it is a number then reveal that number but dont recurse
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def dfs(i, j, m, n, vals, board):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] == "M" or board[i][j] == "B":
                return
            if vals[i][j] != 0:
                board[i][j] = str(vals[i][j])
                return
            board[i][j] = "B"
            dfs(i, j+1, m, n, vals, board)
            dfs(i, j-1, m, n, vals, board)
            dfs(i-1, j, m, n, vals, board)
            dfs(i+1, j, m, n, vals, board)
            dfs(i+1, j+1, m, n, vals, board)
            dfs(i+1, j-1, m, n, vals, board)
            dfs(i-1, j+1, m, n, vals, board)
            dfs(i-1, j-1, m, n, vals, board)


        def adj_bomb_squares(i, j, m, n, board, vals):
            dirs = [[-1, 0], [1,0], [0,1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            for dir in dirs:
                x = j - dir[1]
                y = i - dir[0]
                if x >= 0 and y >= 0 and x < n and y < m:
                    curr_val = board[y][x]
                    if curr_val == "E":
                        vals[y][x] += 1
        m = len(board)
        n = len(board[0])
        vals = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == "M":
                    adj_bomb_squares(i, j, m, n, board, vals)
                if board[i][j] != "B" and board[i][j] != "E":
                    vals[i][j] = board[i][j]
        print(vals)
        click_i = click[0]
        click_j = click[1]
        if board[click_i][click_j] == "M":
            board[click_i][click_j] = "X"
            return board
        dfs(click[0], click[1], m, n, vals, board) 
        return board

