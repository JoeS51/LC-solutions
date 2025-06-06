# - find max first
# sliding window
# increment l in for loop
# r pointer should increase until it is met

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)

        r = 0
        curr_count = 0
        total_count = 0
        for l in range(len(nums)):
            if l > 0:
                if nums[l - 1] == max_num:
                    curr_count -= 1
            while r < len(nums) and curr_count < k:
                if nums[r] == max_num:
                    curr_count += 1
                r += 1
            if r >= len(nums) and curr_count < k:
                continue
            total_count += len(nums) - r + 1
        return total_count
        

