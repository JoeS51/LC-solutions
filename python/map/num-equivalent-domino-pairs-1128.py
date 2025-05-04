class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = defaultdict(int)
        count = 0
        for i in range(len(dominoes)):
            a, b = dominoes[i][0], dominoes[i][1]
            key = tuple(sorted((a, b)))  # Normalize the domino
            count += seen[key]           # Add all previously seen equivalent pairs
            seen[key] += 1   
            
        return count

# runtime: O(n)
# spacetime: O(n)

# you can use sorted to make sure that the map stores both possible options and keep (2,1) and (1,2) at consistent counts
