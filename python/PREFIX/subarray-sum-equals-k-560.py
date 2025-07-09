# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
#  
# 
# Example 1:
# 
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# 
# Input: nums = [1,2,3], k = 3
# Output: 2
#  
# 
# Constraints:
# 
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
# from typing import List
# 
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         def binary_search(arr, val):
#             lo, hi = 0, len(arr)
#             while lo < hi:
#                 mid = (lo+hi) // 2
#                 if arr[mid] < val:
#                     lo = mid + 1
#                 else:
#                     hi = mid
#             return lo
# 
#         prefix_sum = [0]
#         m = {}
#         sum = 0
#         for i in range(len(nums)):
#             sum += nums[i]
#             prefix_sum.append(sum)
#             if sum not in m:
#                 m[sum] = []
#             m[sum].append(i)
#         temp = binary_search([1,2,3], 1)
# #        print("binary search result")
# #        print(temp)
# 
#         res = 0
#         for i in range(len(prefix_sum)):
#             curr_sum = prefix_sum[i]
#             desired_val = curr_sum + k
#             if desired_val in m:
#                 # binary search here to find numbers past curr index
#                 arr = m[desired_val]
#                 start_i = binary_search(arr, i)
#                 count = 0
#                 if arr[start_i] == start_i:
#                     count = -1
#                 count = len(arr) - start_i
#                 res += count
#         return res
# 
# if __name__ == "__main__":
#     sol = Solution()
#     #print("answers")
#     print(sol.subarraySum(list([1,1,1]), 2))
#     #print(sol.subarraySum([1,2,3], 3))


# I overengineered my initial solution. My initial approach was similar but for the map we add all the indices and then when we iterate over the prefixes we look ahead and 
# see all the valid indices. Instead, if we just iterate over it and build the map in one loop then we can check for previous prefix sums that meet our criteria and add that to res
# this way we are not double counting as we just look at previous valid prefix sums 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        m = {0: 1}
        sum = 0
        res = 0
        for i in nums:
            sum += i
            desired = sum - k
            if desired in m:
                res += m[desired]
            m.setdefault(sum, 0)
            m[sum] += 1

        return res

# runtime: O(n)
# spacetime: O(n)



"""
prefix = [0, 1, 3, 6]
k = 3

"""
