class Solution:
    def topoSort(self, V, adj):
        incoming_edges = [0] * V
        for i in range(len(adj)):
            edges = adj[i]
            for j in edges:
                incoming_edges[j] += 1
        print(incoming_edges)

        q = []
        for i in range(len(incoming_edges)):
            curr = incoming_edges[i]
            if curr == 0:
                q.append(i)
        res = [] 
        while q:
            curr = q.pop(0)
            res.append(curr)
            if adj[curr]:
                for i in adj[curr]:
                    incoming_edges[i] -= 1
                    if incoming_edges[i] == 0:
                        q.append(i)
            
        return res
    
if __name__ == "__main__":
    sol = Solution()
    arr = sol.topoSort(6, [[2,3],[3,1],[4,0],[4,1],[5,0],[5,1]])
    print(arr)
 
 
