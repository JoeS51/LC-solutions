class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        nums = sorted(maximumHeight, reverse=True) 
        curr = float('inf')
        total = 0
        for i in nums:
            if i >= curr:
                curr -= 1
                if curr <= 0:
                    return -1
                total += curr 
            else:
                total += i
                curr = i
        return total
# runtime: O(nlogn)
# spacetime: O(n)
