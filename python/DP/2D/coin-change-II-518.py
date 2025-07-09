# recurrence relation
# DP(amount, i) = DP(amount - coins[i], i) or DP(amount, i+1)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i+1][j]
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j-coins[i]]
        return dp[0][amount]

        # @cache
        # def dp(desired_amount, idx):
        #     if 0 == desired_amount:
        #         return 1
        #     if 0 > desired_amount:
        #         return 0
        #     nonlocal coins
        #     total = 0
        #     for i in range(idx, len(coins)):
        #         curr_coin = coins[i]
        #         total += dp(desired_amount - curr_coin, i)
        #     return total
        # return dp(amount, 0)


# runtime: O(n * amount)
# spacetime: O(n * amount)
