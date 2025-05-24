class Solution:
    def maxSubstrings(self, word: str) -> int:
        if len(word) < 4:
            return 0
        curr_chars = {}
        for i in range(3):
            curr_chars.setdefault(word[i], i)

        i = 3
        res = 0
        while i < len(word):
            ch = word[i]
            # can reset here
            if ch in curr_chars and i - curr_chars[ch] >= 3:
                res += 1 
                curr_chars = {}
            elif ch not in curr_chars:
                curr_chars[ch] = i
            i += 1
        return res 

