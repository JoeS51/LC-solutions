class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i, s):
            if i >= len(s):
                return 1
            if i == len(s) - 1:
                return 1 if s[i] != "0" else 0
            curr_char = s[i]            
            next_char = s[i+1]
            combined = s[i] + s[i+1]
            if curr_char == "0":
                return 0
            elif int(combined) > 26:
                return dp(i+1, s)
            else:
                return dp(i+1, s) + dp(i+2, s)
        return dp(0, s)
                
            
                
            
# runtime: O(N)
# spacetime: O(N)

