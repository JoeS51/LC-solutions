class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j, word1, word2) -> int:
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            # replace
            if word1[i] == word2[j]:
                replace = dp(i+1, j+1, word1, word2)
            else:
                replace = 1 + dp(i+1, j+1, word1, word2) 
            # delete
            remove = 1 + dp(i+1, j, word1, word2)
            # add
            add = 1 + dp(i, j+1, word1, word2)
            return min(replace, remove, add)

        return dp(0, 0, word1, word2)
        

