class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for connection in connections:
            adj_list[connection[0]].append(connection[1])
            adj_list[connection[1]].append(connection[0])
        
        def dfs(i, curr_id, ids, components, visited):
            nonlocal adj_list
            if i in visited:
                return
            visited.add(i)
            ids[i] = curr_id
            components[curr_id].add(i)
            if i not in adj_list:
                return
            for next_station in adj_list[i]:
                dfs(next_station, curr_id, ids, components, visited)
        # attach an id to all components
        ids = {}
        components = defaultdict(SortedList)
        curr_id = 0
        for i in range(1, c+1):
            curr_id += 1
            if i in ids:
                continue
            dfs(i, curr_id, ids, components, set())
        status = [0] * (c + 1)
        res = []
        print(components)
        # search queries
        for query in queries:
            q_type, node = query
            if q_type == 2:
                if status[node] == -1:
                    continue
                status[node] = -1
                node_id = ids[node]
                components[node_id].remove(node)
            elif q_type == 1:
                if status[node] == 0:
                    res.append(node)
                else:
                    node_id = ids[node]
                    min_node = components[node_id]
                    if min_node:
                        res.append(min_node[0])
                    else:
                        res.append(-1)
                    # res.append(min_node)


        return res

