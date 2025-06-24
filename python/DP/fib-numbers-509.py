class Solution:
    def fib(self, n: int) -> int:
        @cache
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return dp(n-1) + dp(n-2)
        return dp(n)
        
runtime: O(n)
