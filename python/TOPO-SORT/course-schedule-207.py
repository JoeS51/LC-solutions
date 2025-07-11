class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topo sort with detecting cycle
        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        for i in prerequisites:
            next_course = i[0]
            prereq = i[1]
            if next_course == prereq:
                return False
            adj_list[prereq].append(next_course)
            indegree[next_course] += 1

        q = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        count = 0 
        res = []
        while q:
            count += 1
            curr = q.pop(0)
            res.append(curr)
            for i in adj_list[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return count == numCourses

# runtime: O(V+E)
# spacetime: O(V+E)

        

