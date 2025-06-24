class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = Counter(nums)
        unique = sorted(count)

        @lru_cache(maxsize=None)
        def dfs(i):
            if i >= len(unique):
                return 0
            
            # Take this number
            points = count[unique[i]] * unique[i]
            if i + 1 < len(unique) and unique[i] + 1 == unique[i + 1]:
                take = points + dfs(i + 2)
            else:
                take = points + dfs(i + 1)

            # Skip this number
            skip = dfs(i + 1)

            return max(take, skip)

        return dfs(0)


# runtime: O(n)
# spacetime: O(n)
