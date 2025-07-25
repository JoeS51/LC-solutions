class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        max_bin = k
        zero_count = 0
        res = 0
        curr_bin = 0
        n = len(s)
        for i in range(len(s)):
            if s[i] == "1":
                curr_bin += 2 ** (n-i-1)
        
        for i in range(len(s)):
            if curr_bin > max_bin:
                if s[i] == "0":
                    zero_count += 1
                else:
                    curr_bin -= 2 ** (n-i-1)
            else:
                right_side = n - i
                left_side = zero_count
                return right_side + left_side
        return -1

        
# runtime: O(N)
# spacetime: O(1)
