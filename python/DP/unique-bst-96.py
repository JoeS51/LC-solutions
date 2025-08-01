class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            curr_dp = 0
            for j in range(1, i+1):
                left = dp[j-1]
                right = dp[i-j]
                curr_dp += left * right
            dp[i] = curr_dp
        return dp[n]
        
# runtime: O(N^2) 
# spacetime: O(N)
