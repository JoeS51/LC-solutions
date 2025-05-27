class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if not edges and colors:
            return 1
        val_map = {}
        for i in range(len(colors)):
            val_map[i] = colors[i]
        adj_list = {}
        for start, end in edges:
            adj_list.setdefault(start, []).append(end)

        res = -1
        visited = [0] * len(colors)
        curr_vals = defaultdict(int)
        has_cycle = False

        memo = {}

        def dfs(curr):
            nonlocal has_cycle
            # cycle
            if visited[curr] == 1:
                has_cycle = True
                return [0] * 26

            # cached
            if visited[curr] == 2:
                return memo[curr]
            
            visited[curr] = 1
            color_counts = [0] * 26

            if curr not in adj_list:
                visited[curr] = 2
                i = ord(val_map[curr]) - ord('a')
                color_counts[i] += 1
                memo[curr] = color_counts
                return color_counts
            for neighbor in adj_list[curr]:
                child_counts = dfs(neighbor)
                for c in range(26):
                    color_counts[c] = max(color_counts[c], child_counts[c])
            visited[curr] = 2
            memo[curr] = color_counts
            i = ord(val_map[curr]) - ord('a')
            color_counts[i] += 1
            return color_counts

        res = 0
        for node in adj_list:
            counts = dfs(node)
            res = max(res, max(counts))
        if has_cycle:
            return -1 
        return res
