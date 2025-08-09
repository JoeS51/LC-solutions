class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        parcels = 0
        curr_max = -1
        for i in range(len(weight)):
            curr = weight[i]
            if curr_max == -1:
                curr_max = curr
            if curr_max != -1 and curr < curr_max:
                parcels+=1
                curr_max = -1
            else:
                curr_max = max(curr, curr_max)
        return parcels
        

