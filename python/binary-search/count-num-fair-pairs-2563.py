class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search(nums, lo, hi, val):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] >= val:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo # returns one plus hi in this case which goes back to value that equals mid
        
        nums.sort()
        count_pairs = 0
        for i in range(len(nums)):
            curr_val = nums[i]
            low = binary_search(nums, i+1, len(nums) - 1, lower - curr_val)
            high = binary_search(nums, i+1, len(nums) - 1, upper - curr_val + 1)
            count_pairs += high - low
        return count_pairs
        
# runtime: O(nlogn)
# spacetime: O(1)
