class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        in_edges = [0] * numCourses
        for start, end in prerequisites:
            adj_list[start].append(end)
            in_edges[end] += 1

        q = []
        prereqs = {} 
        for course, val in enumerate(in_edges):
            if val== 0:
                q.append(course)
                prereqs[course] = set()
        while q:
            curr_course = q.pop(0)
            if curr_course in adj_list:
                for next_course in adj_list[curr_course]:
                    in_edges[next_course] -= 1
                    if in_edges[next_course] == 0:
                        q.append(next_course)
                    if next_course not in prereqs:
                        prereqs[next_course] = set()
                    prereqs[next_course].add(curr_course)
                    curr_prereqs = prereqs[curr_course]
                    print(next_course)
                    prereqs[next_course].update(curr_prereqs)
        res = [] 
        for start, end in queries:
            if start in prereqs[end]:
                res.append(True)
            else:
                res.append(False)

        return res

        

