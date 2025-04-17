# brute force
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                if nums[i] == nums[j] and ((i*j) % k == 0):
                    count += 1
        return count
# there is only a O(n^2) solution

        count  = 0
        for i,j in combinations(range(len(nums)),2):
            print(str(i) + " " + str(j))
        return count
# combinations is a cool python method that lets you generate pairs of combinations for a list
