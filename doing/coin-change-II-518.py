# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# 
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# The answer is guaranteed to fit into a signed 32-bit integer.
# 
#  
# 
# Example 1:
# 
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:
# 
# Input: amount = 10, coins = [10]
# Output: 1

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        combos = {}
        #def dp(curr_amount, desired_amount, curr_coins):
        def dp(curr_amount, desired_amount, curr_coins):
            if curr_amount == desired_amount:
                #if curr_coins in combos:
                    #return 0
                combos[curr_coins] = 1
                print(curr_coins)
                return 1
            if curr_amount > desired_amount:
                return 0
            nonlocal coins
            total = 0
            for i in coins:
                #curr_coins.add(i)
                #total += dp(curr_amount + i, desired_amount, curr_coins)
                new_coins= curr_coins
                new_coins.setdefault(i, 0)
                new_coins[i] += 1
                total += dp(curr_amount + i, desired_amount, new_coins)
                new_coins[i] -= 1
                if new_coins[i] == 0:
                    del new_coins[i]
            return total
            

        #return dp(0, amount, set())
        return dp(0, amount, {})

if __name__ == "__main__":
    sol = Solution()
    print(sol.change(5, [1,2,5]))

