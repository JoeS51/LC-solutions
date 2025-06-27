class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            return dp(n-1) + dp(n-2)
        return dp(n)
        
runtime: O(n) because each call to n is cached so it's only computed once
