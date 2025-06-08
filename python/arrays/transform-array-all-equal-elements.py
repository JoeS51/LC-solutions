class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def countEqual(nums, switch_num):
            # count distances between each 
            prev = -1
            res = 0
            for i, val in enumerate(nums):
                if val == switch_num and prev == -1:
                    prev = i
                elif val == switch_num:
                    res += i - prev
                    prev = -1
            return res
            
        count_neg = 0
        count_pos = 0
        for i in nums:
            if i < 0:
                count_neg += 1
            else:
                count_pos += 1
        if count_neg % 2 != 0 and count_pos % 2 != 0:
            return False
        switch_num = -1
        if count_neg % 2 == 0 and count_pos % 2 == 0:
            switch_num = -1 if count_neg < count_pos else 1 
            res = min(countEqual(nums, 1), countEqual(nums, -1))
            if res <= k:
                return True
            else:
                return False
        elif count_pos % 2 == 0:
            switch_num = 1

        res = countEqual(nums, switch_num)
        if res <= k:
            return True
        else:
            return False

        
        
