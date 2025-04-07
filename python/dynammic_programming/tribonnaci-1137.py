class Solution:
    def tribonacci(self, n: int) -> int:
        arr = []
        arr.append(0)
        arr.append(1)
        arr.append(1)
        for i in range(3, n+1):
            arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        return arr[n]

# runtime: O(n)
# spacetime: O(n)
# notes: range() in python does not include n so we need to go to n+1



# the topdown solution
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         dp = {0: 0, 1: 1, 2: 1}
#         def dfs(i):
#             if i in dp:
#                 return dp[i]
#             dp[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
#             return dp[i]
#         
#         return dfs(n)
