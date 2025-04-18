# [0, 0, 0, 0, 0]
# [0, 2, 0, 0, -2]
# [0, 2, 3, 0, -2] = sum_list

# curr_sum = 3
# [0, 2, 5, 5, 3]
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        sum_list = [0] * length
        for update in updates:
            start = update[0]
            end = update[1] + 1
            add = update[2]
            sum_list[start] += add
            if end < length:
                sum_list[end] -= add
        res_list = []
        curr_sum = 0
        for i in sum_list:
            curr_sum += i
            res_list.append(curr_sum)
        return res_list


