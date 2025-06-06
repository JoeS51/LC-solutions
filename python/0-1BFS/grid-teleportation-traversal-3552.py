class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        teleports = {}
        dist = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j].isalpha():
                    teleports.setdefault(matrix[i][j], []).append((i, j))

        visited_teleport = set()
        q = deque([(0, 0)])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist[0][0] = 0
        while q:
            i, j = q.popleft()
            curr_char = matrix[i][j]
            curr_dist = dist[i][j]
            if 0 <= i < m and 0 <= j < n and curr_char != "#":
                if i == m-1 and j == n-1:
                    return dist[i][j]
                # if letter then you can teleport
                if curr_char.isalpha() and curr_char not in visited_teleport:
                    for di, dj in teleports[curr_char]:
                        if (di, dj) == (i, j):
                            continue
                        if dist[di][dj] > curr_dist:
                            dist[di][dj] = curr_dist
                            q.appendleft((di, dj))
                    visited_teleport.add(curr_char)
                for x, y in dirs:
                    new_i = x + i
                    new_j = y + j
                    if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] != "#":
                        if dist[new_i][new_j] > dist[i][j] + 1:
                            dist[new_i][new_j] = curr_dist + 1
                            q.append((new_i, new_j))
        return -1

# runtime: O(N*M)
# spacetime: O(N*M)
