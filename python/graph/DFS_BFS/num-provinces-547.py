class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, adj_map, visited):
            if i in visited:
                return
            visited.add(i)
            for city in adj_map[i]:
                dfs(city, adj_map, visited)
            return
            
        adj_map = {}
        for i, val in enumerate(isConnected):
            for j, val2 in enumerate(isConnected[i]):
                if i not in adj_map:
                    adj_map[i] = list()
                if val2 == 1:
                    adj_map[i].append(j)
        print(adj_map)
        visited = set()
        num_connected = 0
        for i in adj_map:
            if i not in visited:
                num_connected += 1
                dfs(i, adj_map, visited)
        return num_connected


        
# time complexity: O(n^2)
# space complexity: O(n^2)
