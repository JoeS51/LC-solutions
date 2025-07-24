class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        curr = nums[0] + 1
        i = 1
        while k > 0:
            if i < len(nums) and nums[i] == curr:
                i += 1
                curr += 1
            elif i < len(nums) and k < nums[i] - nums[i-1]:
                return nums[i-1] + k
            else:
                if i == len(nums):
                    return k + nums[i-1]
                k -= (nums[i] - nums[i-1] - 1)
                curr = nums[i] + 1
                i += 1
        return curr
            

        

