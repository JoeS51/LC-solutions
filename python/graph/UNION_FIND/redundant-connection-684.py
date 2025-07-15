class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n+1)]
        self.size = [1] * (n+1)

    def find(self, A):
        if self.parent[A] == A:
            return A
        self.parent[A] = self.find(self.parent[A])
        return self.parent[A]

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return False
        
        if self.size[root_A] > self.size[root_B]:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        else:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for edge in edges:
            n = max(n, max(edge[0], edge[1]))

        uf = UnionFind(n) 
        for A,B in edges:
            res = uf.union(A, B)
            if not res:
                return [A,B]
        return []
        

# runtime: O(nlogn) or almost constant for union find so O(n)
# spacetime: O(n)
