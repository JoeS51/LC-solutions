class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        distances = {(i,j): float('inf') for i in range(m) for j in range(n)}
        pq = [(0, (0, 0))]
        dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        visited = set()
        while pq:
            wait_time, curr_coordinates = heapq.heappop(pq)
            if curr_coordinates in visited:
                continue
            visited.add(curr_coordinates)
            if curr_coordinates[0] == m-1 and curr_coordinates[1] == n-1:
                return wait_time
            for dir in dirs:
                next_x = curr_coordinates[0] + dir[0]
                next_y = curr_coordinates[1]+ dir[1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                next_node_coord = (next_x, next_y)
                next_node_w = max(moveTime[next_x][next_y], wait_time)
                if next_node_coord in visited:
                    continue
                heapq.heappush(pq, (next_node_w+1, next_node_coord))
        return 1
        


