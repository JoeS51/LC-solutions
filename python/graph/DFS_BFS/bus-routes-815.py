# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
# 
# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.
# 
# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
# 
# 
# Example 1:
# 
# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:
# 
# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1



"""
adj_list = {
    1: [(2, 0)]
    2: [(7, 0)]
    7: [(1, 0), (3, 1)]
    3: [(6, 1)]
    6: [(7, 1)]
}
"""

from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        adj_list = defaultdict(list)
        curr_route = 0
        for route, val in enumerate(routes):
            for stop in val:
                adj_list[stop].append(route)
        
        q = deque([])
        for i in adj_list[source]:
            q.append((i, 1))

        desired = set()
        for j in adj_list[target]:
            desired.add(j)

        visited = set()
        while q:
            curr_route, cost = q.popleft()
            if curr_route in desired:
                return cost
            for next_stop in routes[curr_route]:
                next_routes = adj_list[next_stop]
                for route in next_routes:
                    if route in visited:
                        continue
                    visited.add(route)
                    q.append((route, cost+1))
        return -1



