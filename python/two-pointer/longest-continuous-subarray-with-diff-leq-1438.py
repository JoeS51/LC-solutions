# initial solution
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest_subarray_len = 0
        l = 0
        min_heap = []
        max_heap = []
        curr_map = defaultdict(int)
        count = 0 
        for r in range(len(nums)):
            curr_num = nums[r]
            heapq.heappush(min_heap, curr_num)
            heapq.heappush(max_heap, -curr_num)
            curr_map[curr_num] += 1
            curr_min = heapq.heappop(min_heap)
            while len(min_heap) > 0 and curr_map[curr_min] == 0:
                curr_min = heapq.heappop(min_heap)
            curr_max = heapq.heappop(max_heap)
            while len(max_heap) > 0 and curr_map[-curr_max] == 0:
                curr_max = heapq.heappop(max_heap)
            heapq.heappush(min_heap, curr_min)
            heapq.heappush(max_heap, curr_max)
            while l < r and (-curr_max - curr_min) > limit:
                curr_map[nums[l]] -= 1
                while len(min_heap) > 0 and curr_map[curr_min] == 0:
                    curr_min = heapq.heappop(min_heap)
                while len(max_heap) > 0 and curr_map[-curr_max] == 0:
                    curr_max = heapq.heappop(max_heap)
                heapq.heappush(min_heap, curr_min)
                heapq.heappush(max_heap, curr_max)
                l += 1
            count = max(count, r - l + 1)
        return count

# TODO LOOK AT BETTER SOLUTION
