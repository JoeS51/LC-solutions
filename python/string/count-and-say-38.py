# "1" -> one 1
# "11" -> 21
# "21" -> 1211
# "1211" -> 111221 


class Solution:
    def countAndSay(self, n: int) -> str:
        def convert_to_RLE(curr: str) -> str:
            i = 0
            res_str = ""
            while i < len(curr):
                if i == len(curr) - 1:
                    res_str += "1" + curr[i]
                else:
                    original_num = curr[i]
                    count_num = 1
                    while i+1 < len(curr) and curr[i+1] == original_num:
                        i += 1
                        count_num += 1
                    res_str += str(count_num) + original_num
                i += 1
            return res_str
        curr_str = "1"
        for i in range(n-1):
            curr_str = convert_to_RLE(curr_str)
        return curr_str


