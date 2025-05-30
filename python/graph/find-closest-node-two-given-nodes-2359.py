class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj_list = {}
        for i in range(len(edges)):
            adj_list[i] = edges[i]
        node1_map = defaultdict(int) 
        count = 0 
        def dfs(node):
            # cycle
            nonlocal count
            count += 1
            if node in node1_map:
                return -1
            node1_map[node] = count
            if adj_list[node] != -1:
                dfs(adj_list[node])
        node2_map = defaultdict(int)
        count2 = 0
        min_count = float('inf')
        min_node = -1
        def node2_dfs(node):
            nonlocal count2
            nonlocal min_count
            nonlocal min_node
            count2 += 1
            if node in node2_map:
                return -1
            node2_map[node] = count2
            if node == -1:
                return -1
            if node in node1_map:
                curr_count = max(node1_map[node], node2_map[node])
                if curr_count <= min_count:
                    if curr_count == min_count and node < min_node:
                        min_node = node
                        min_count = curr_count
                    elif curr_count < min_count: 
                        min_node = node
                        min_count = curr_count
            return node2_dfs(adj_list[node])
        dfs(node1)
        node2_dfs(node2)
        return min_node
        

# optimal solution (dont even need to do dfs

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [-1] * n
        dist2 = [-1] * n

        def compute_distances(start, dist):
            d = 0
            curr = start
            while curr != -1 and dist[curr] == -1:
                dist[curr] = d
                d += 1
                curr = edges[curr]

        compute_distances(node1, dist1)
        compute_distances(node2, dist2)

        min_dist = float('inf')
        result = -1

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist or (max_dist == min_dist and i < result):
                    min_dist = max_dist
                    result = i

        return result

