import functools

class Solution:
	def getCount(self, n):
		# code here
		adj_map = {}
		adj_map[0] = [0, 8]
		adj_map[1] = [1, 2,4]
		adj_map[2] = [1,2,3,5]
		adj_map[3] = [2,3,6]
		adj_map[4] = [1,4,5,7]
		adj_map[5] = [2,4,5,6,8]
		adj_map[6] = [3,5,6,9]
		adj_map[7] = [4,7,8]
		adj_map[8] = [0, 5,7,8,9]
		adj_map[9] = [6,8,9]
		
        @functools.lru_cache(maxsize=None)
        def dfs(curr, n):
		    nonlocal adj_map
		    if n <= 0:
		      #  print(s)
		        return 1
		    curr_total = 0
		    for neigh in adj_map[curr]:
		        curr_total += dfs(neigh, n-1)
		    return curr_total
		total = 0
		for i in range(0, 10):
		    total += dfs(i, n-1)
		return total

# runtime: O(n)?
# spacetime: O(n)
