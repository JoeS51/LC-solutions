class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        total = 0
        l = 0
        
        for r in range(n):
            while l <= r and (prefix_sum[r + 1] - prefix_sum[l]) * (r - l + 1) >= k:
                l += 1
            total += (r - l + 1)
        
        return total

