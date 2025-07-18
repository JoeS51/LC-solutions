class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # start with bottom right 
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        curr_max = 0
        for i in range(m):
            if matrix[n-1][i] == "1":
                curr_max = 1
            dp[n-1][i] = 0 if matrix[n-1][i] == "0" else 1
        
        for i in range(n):
            if matrix[i][m-1] == "1":
                curr_max = 1
            dp[i][m-1] = 0 if matrix[i][m-1] == "0" else 1

        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if matrix[i][j] == "0":
                    continue
                else: 
                    dp[i][j] = min(dp[i+1][j], min(dp[i+1][j+1], dp[i][j+1])) + 1
                    curr_max = max(curr_max, dp[i][j])
        return curr_max * curr_max

# TODO
