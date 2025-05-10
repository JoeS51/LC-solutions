"""
- iterate over adj_list and dfs until you are less than t or you're above the edge weights
"""




class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:

        if t > 0 and k == 0:
            return 0
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
        @lru_cache(maxsize=None)
        def dfs(curr_node, curr_k, curr_t, k, t):
            if curr_k == k and curr_t < t:
                return curr_t
            if curr_k > k:
                return -1
            if curr_t >= t:
                return -1
            if curr_node not in adj_list:
                if k == curr_k:
                    return curr_t
                else:
                    return -1
            max_val = -1
            for next_node in adj_list[curr_node]:
                curr = dfs(next_node[0], curr_k + 1, curr_t + next_node[1], k, t)
                max_val = max(max_val, curr)
            return max_val 

        max_val = -1
        for start_node in adj_list:
            curr_val = dfs(start_node, 0, 0, k, t)
            if curr_val > t:
                continue
            if curr_val + 1 == t:
                return t - 1
            max_val = max(curr_val, max_val)
        return max_val
        

