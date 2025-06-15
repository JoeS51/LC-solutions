class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        m = {}
        for ind, i in enumerate(nums):
            target = i * 2
            if target in m:
                arr[ind] = m[target]
            if i not in m:
                m[i] = 0 
            m[i] += 1
        res = 0
        for i in range(len(nums)):
            if arr[i] == 0:
                continue
            if nums[i] != 0:
                left = arr[i]
                target = nums[i] * 2
                right = m[target] - left
                res += left * right
            else:
                left = arr[i]
                right = m[0] - left - 1
                res += left * right
                
        MOD = 10 ** 9 + 7
        return res % MOD
        
# runtime: O(n)
# spacetime: O(n)
