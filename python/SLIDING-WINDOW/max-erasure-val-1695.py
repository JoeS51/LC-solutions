class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr_set = set()
        l = 0
        curr_set.add(nums[0])
        total = nums[0]
        max_total = total
        for r in range(1, len(nums)):
            curr_num = nums[r]
            while l < len(nums) and curr_num in curr_set and nums[l] != curr_num:
                curr_set.remove(nums[l])
                total -= nums[l]
                l += 1
            if nums[l] == curr_num and l < len(nums):
                total -= nums[l]
                l += 1
            elif l >= len(nums):
                return max_total
            total += curr_num
            curr_set.add(nums[r])
            max_total = max(max_total, total)
        return max_total
        

