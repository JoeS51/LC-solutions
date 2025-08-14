class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev = float('inf')
        print(nums)
        for i in range(len(nums) - 2):
            curr_num = nums[i]
            if curr_num == prev:
                continue
            prev = curr_num
            l = i + 1
            r = len(nums) - 1
            curr_total = curr_num + nums[l] + nums[r]
            while l < r:
                if curr_total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif curr_total < 0:
                    l += 1
                else:
                    r -= 1
                curr_total = curr_num + nums[l] + nums[r]
                
        return res 

# runtime: O(N^2)
# spacetime: O(1)
