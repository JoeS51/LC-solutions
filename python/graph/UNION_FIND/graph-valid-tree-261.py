class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n
    
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
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_B]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        unionFind = UnionFind(n)

        for A, B in edges:
            res = unionFind.union(A, B)
            if not res:
                return False
        return True

        

