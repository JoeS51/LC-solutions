class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
       map = dict()
       for i, val in enumerate(keyboard):
        map[val] = i
       curr = 0
       sum = 0
       for w in word:
        if not map.get(w) is None:
            sum += abs(map.get(w) - curr)
            curr = map.get(w)
       return sum

# Big O: O(n)
# Space complexity: O(n)