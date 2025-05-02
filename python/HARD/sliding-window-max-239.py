"""
[1,3,-1,-3,4,3,6,7]
map = {3: 1, -1: 1, -3}
heap = [3, 1, -1, -3]
"""




class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [] 
        counts = defaultdict(int)
        for i in range(k):
            heappush(heap, -nums[i])
            counts[nums[i]] += 1
        res = []
        res.append(-heap[0]) 
        l = 0
        for r in range(k, len(nums)):
            curr_num = nums[r]
            remove_num = nums[l]
            heappush(heap, -curr_num)
            counts[curr_num] += 1
            counts[remove_num] -= 1
            while len(heap) > 0 and counts[-heap[0]] <= 0:
                heappop(heap)
            res.append(-heap[0])
            l += 1
        return res
# TODO: add runtime
