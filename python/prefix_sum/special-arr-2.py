class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def isEven(n):
            return n%2 == 0
        prefix_sum = []
        boolean_arr = []
        boolean_arr.append(False)
        for i in range(1, len(nums)):
            prev = isEven(nums[i-1])
            curr = isEven(nums[i])
            if prev != curr:
                boolean_arr.append(False)
            else:
                boolean_arr.append(True)
        prefix_sum.append(0)
        for i in range(1, len(boolean_arr)):
            prev_val = prefix_sum[i-1]
            curr_val = int(boolean_arr[i]) 
            prefix_sum.append(prev_val + curr_val)
        print(prefix_sum)
        res = [] 
        for s, e in queries:
            if prefix_sum[s] < prefix_sum[e]:
                res.append(False)
            else:
                res.append(True)
        return res

