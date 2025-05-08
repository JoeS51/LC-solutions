class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[k] = 0
        pq = [(0, k)]

        adj_list = {}
        for time in times:
            u, v, w = time[0], time[1], time[2]
            if u in adj_list:
                adj_list[u].append((v, w))
            else:
                adj_list[u] = [(v, w)]

        while pq:
            dist, curr_node = heapq.heappop(pq)

            if curr_node not in adj_list:
                continue
            if dist > distances[curr_node]:
                continue
            next_nodes = adj_list[curr_node]
            for v, w in next_nodes:
                new_dist = dist + w
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
        max_dist = max(distances.values())
        return -1 if max_dist == float('inf') else max_dist

