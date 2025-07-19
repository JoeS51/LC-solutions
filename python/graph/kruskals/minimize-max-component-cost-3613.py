class UnionFind:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [n for n in range(n)]
    def find(self, A):
        if self.parent[A] == A:
            return A
        self.parent[A] = self.find(self.parent[A])
        return self.parent[A]
    def union(self, A, B, cost):
        root_A = self.find(A)
        root_B = self.find(B)
        print()
        if root_A == root_B:
            return True
        if self.rank[root_A] >= self.rank[root_B]:
            self.rank[root_B] = max(cost, self.rank[root_A])
            self.rank[root_A] = max(cost, self.rank[root_A])
            self.parent[root_B] = root_A
        elif self.rank[root_B] > self.rank[root_A]:
            self.rank[root_A] = max(self.rank[root_B], cost)
            self.rank[root_B] = max(cost, self.rank[root_B])
            self.parent[root_A] = root_B
        return False
    def getcost(self):
        m = defaultdict(int)
        print(self.parent)
        print(self.rank)
        for i in range(len(self.parent)):
            self.find(i)
            m[self.parent[i]] = max(self.rank[i], m[self.parent[i]])
        res = 0
        for e in m:
            res = max(res, m[e])
        return res



class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        sorted_edges = sorted(edges, key = lambda x: x[2])
        adj_list = defaultdict(list)
        unionFind = UnionFind(n)
        num_components = n
        i = 0
        print(sorted_edges)
        while num_components != k:
            edge = sorted_edges[i]
            start = edge[0]
            end = edge[1]
            cost = edge[2]
            res = unionFind.union(start, end, cost)
            i += 1
            if res:
                continue
            print(edge)
            num_components -= 1
        return unionFind.getcost()

