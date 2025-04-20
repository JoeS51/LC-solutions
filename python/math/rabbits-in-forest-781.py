class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        nums = {}
        res = 0
        for i in answers:
            if i == 0:
                res += 1
                continue
            if i not in nums or nums[i] == 0:
                res += i +1
                nums[i] = i
            else:
                nums[i] -= 1

        return res
        

