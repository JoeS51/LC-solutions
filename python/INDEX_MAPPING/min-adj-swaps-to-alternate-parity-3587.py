class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def helper(indices):
            cost = 0
            for i in range(len(indices)):
                desired = i * 2 # this is the position this parity should be at
                cost += abs(indices[i] - desired)
            return cost

        evens = []
        odds = []
        for i in range(len(nums)):
            curr = nums[i]
            if curr % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        size_diff = len(evens) - len(odds)
        if abs(size_diff) > 1:
            return -1
        ans = -float('inf')
        # check both configurations
        if size_diff == 0:
            e = helper(evens)
            o = helper(odds)
            return min(e, o)
        elif size_diff == 1: # should be in order of even, odd, even
            return helper(evens)
        else: # order should be odd, evens, odd
            return helper(odds)

# runtime: O(N)
# spacetime: O(N)
        

