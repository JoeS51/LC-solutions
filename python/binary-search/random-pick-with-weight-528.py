class Solution:

    def __init__(self, w: List[int]):
        self.sums = []
        self.total = sum(w)
        self.w = w
        curr_sum = 0
        for weights in w:
            curr_sum += weights
            self.sums.append(curr_sum)


    def pickIndex(self) -> int:
        num = self.total * random.random()
        l, r = 0, len(self.sums)

        # [1, 2, 4]
        # [1, 3, 7]
        while (l < r):
            mid = (l + r) // 2
            if self.sums[mid] - 1 == num:
                return mid 
            elif self.sums[mid] > num:
                r = mid 
            else:
                l = mid +  1
        return l


        

# [1, 3]
# [{1}, {1, 1, 1}]
# 3


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

