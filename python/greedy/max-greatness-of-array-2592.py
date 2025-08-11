class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        init = 0
        counts = Counter(nums)
        s = set(nums)
        total = 0
        initial = True
        for i in s:
            if initial:
                init += counts[i]
                initial = False
            else:
                curr_count = counts[i]
                diff = min(curr_count, init)
                init = init + curr_count - diff
                total += diff
        return total

# time complexity: O(nlogn)
# space complexity: O(N)
