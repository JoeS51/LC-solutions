class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        r = [(0, 0)] * len(nums)
        l = [(0, 0)] * len(nums)
        dp = [(0,0)] * len(nums)
        l[0] = (nums[0], nums[0])
        for i in range(1, len(nums)):
            curr_num = nums[i]
            min_val = min(l[i-1][0], curr_num)
            max_val = max(l[i-1][1], curr_num)
            l[i] = (min_val, max_val)
            
        r[len(nums)-1] = (nums[len(nums)-1], nums[len(nums)-1])
        for i in range(len(nums) - 2, -1, -1):
            curr_num = nums[i]
            min_val = min(r[i+1][0], curr_num)
            max_val = max(r[i+1][1], curr_num)
            r[i] = (min_val, max_val)

        res = -float('inf')
        for i in range(len(nums)):
            next_i = i + (m-1)
            if next_i >= len(nums):
                break
            r_min, r_max = r[next_i][0], r[next_i][1]
            l_min, l_max = l[i][0], l[i][1]
            dp[i] = (r_min * l_min, r_max * l_max)
            res = max(res, max(dp[i][1], dp[i][0]))
            
        return res
            
        
# runtime: O(n)
# spacetime: O(n)
