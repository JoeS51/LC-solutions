class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count

# runtime: O(n * log m) apparently converting int to str is log time
# spacetime: O(1)
