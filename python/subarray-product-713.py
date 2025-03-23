class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        product = 1
        count = 0

        for r in range(len(nums)):
            product *= nums[r] 
           
            while product >= k and l <= r:
                product /= nums[l]
                l += 1
            count += r - l + 1

        return count
        

# interesting problem using this r-l+1 method allows for you to account for every possibility of subarrays in that range
