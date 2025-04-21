class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        diff_list = []
        curr_sum = 0
        for i in differences:
            curr_sum += i
            diff_list.append(curr_sum)
        min_i = min(diff_list) 
        max_i = max(diff_list)

        min_val = max(lower, lower - min_i)
        max_val = min(upper, upper - max_i)

        return 0 if min_val > max_val else max_val - min_val + 1

