class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        matrix =[[0] * n for _ in range(n)]
        for i, word in enumerate(words):
            if len(word) > n:
                return False
            for j, char in enumerate(word):
                matrix[i][j] = char
        for i in range(n):
            row = matrix[i]
            col = [row[i] for row in matrix]
            if row != col:
                return False
        return True

# Time complexity: O(n^2)
# Space complexity: O(n^2)