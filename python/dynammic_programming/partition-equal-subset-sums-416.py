class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums, i, curr, target):
            if curr == target:
                return True
            elif curr > target or i >= len(nums):
                return False
            return dfs(nums, i+1, curr + nums[i], target) or dfs(nums, i+1, curr, target)
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        half = total_sum / 2
        return dfs(tuple(nums), 0, 0, half)

# memoized solution
