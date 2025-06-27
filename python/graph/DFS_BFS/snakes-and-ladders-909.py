class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n ** 2)
        flip = False
        idx = 0
        for r in range(len(board)-1, -1, -1): 
            curr_row = board[r]
            if flip:
                curr_row.reverse()
            for cell in curr_row:
                cells[idx] = cell
                idx += 1
            flip = not flip
        print(cells)

        q = deque()
        q.append((0, 0))
        dist = [0] * len(cells)
        visited = set()
        # bfs
        while q:
            curr_cell, curr_dist = q.popleft()
            if curr_cell in visited:
                continue
            visited.add(curr_cell)
            if curr_cell == len(cells) - 1:
                return curr_dist
            for next_cell in range(1, 7):
                next_idx = curr_cell + next_cell
                if next_idx >= len(cells):
                    continue
                if cells[next_idx] != -1:
                    q.append((cells[next_idx]-1, curr_dist + 1))
                    dist[cells[next_idx]-1] = curr_dist + 1
                else:
                    q.append((next_idx, curr_dist + 1))
                    dist[next_idx] = curr_dist + 1


        return -1
            
        
# runtime: O(N^2)
# spacetime: O(N^2)
