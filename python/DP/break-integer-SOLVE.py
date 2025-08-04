class Solution:
    def integerBreak(self, n: int) -> int:
        arr = []
        m = n
        def dp(n):
            if n == 0:
                product = 1
                for i in arr:
                    product *= i
                return product
            if n < 0:
                return 0
            res = 0
            for i in range(1, m):
                if n - i < 0:
                    break
                arr.append(i)
                curr_val = dp(n - i)
                arr.pop()
                res = max(res, curr_val)
            return res
        
        return dp(n)
        
