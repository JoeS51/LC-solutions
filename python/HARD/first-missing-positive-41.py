class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_pos = float('inf')
        max_pos = -1
        cnt = [0] * 100001
        for i in nums:
            if i < min_pos and i > 0:
                min_pos = i
            if i > max_pos and i > 0:
                max_pos = i
            if 0 < i < 100005:
                cnt[i-1] = 1
        if min_pos == float('inf') or min_pos > 1:
            return 1
        for i in range(len(cnt)):
            if cnt[i] == 0:
                return i+1
        return -1

# runtime: O(n)
# spacetime: O(1)

# notes: Solved this after thinking about it for a bit. The constraints make it pretty hard but there are only so many ways to get O(1) spacetime and O(n) runtime
# TODO: Make sure to find more solutions to this problem and how to optimizie


