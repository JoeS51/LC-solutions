class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0] * len(values)
        curr_max = (values[0] - len(values), 0)
        for i in range(1, len(values)):
            actual_max = values[i] + values[curr_max[1]] + curr_max[1] - i
            dp[i] = max(actual_max, dp[i-1])
            i_val = (values[i] - (len(values) - i), i)
            if curr_max[0] < i_val[0]:
                curr_max = i_val
        print(dp)
        return dp[len(values)-1]

# runtime: O(n)
# spacetime: O(n)
        

