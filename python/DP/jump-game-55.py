class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True
        for i in range(len(nums)-2, -1, -1):
            curr_val = nums[i]
            for j in range(1, curr_val+1):
                next_val = j + i
                if dp[next_val]:
                    dp[i] = True
                    break
        print(dp)
        return dp[0]

        

