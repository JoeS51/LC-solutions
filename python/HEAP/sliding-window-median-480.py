# Simpler sorted list approach
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        curr_nums = SortedList()
        res = []

        for i in range(k):
            curr_nums.add(nums[i])

        if k % 2 == 0:
            mid_1 = curr_nums[k // 2]
            mid_2 = curr_nums[k // 2 - 1] 
            res.append(((mid_1 + mid_2) / 2))
        else:
            res.append(curr_nums[k // 2])

        for i in range(k, len(nums)):
            curr_nums.remove(nums[i-k])
            curr_nums.add(nums[i])
            if k % 2 == 0:
                mid_1 = curr_nums[k // 2]
                mid_2 = curr_nums[k // 2 - 1] 
                res.append(((mid_1 + mid_2) / 2))
            else:
                res.append(curr_nums[k // 2])
        return res

# two heap approach 
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def getMedian(lo, hi, k):
            if k % 2 == 0:
                first = -lo[0]
                second = hi[0]
                return (first + second) / 2
            else:
                return -lo[0]

        lo = [] # max heap
        hi = [] # min heap
        counts = defaultdict(int)

        for i in range(k):
            heapq.heappush(lo, -nums[i])

        for i in range(k // 2):
            heapq.heappush(hi, -heapq.heappop(lo))

        res = []
        res.append(getMedian(lo, hi, k))

        for i in range(k, len(nums)):
            out_num = nums[i-k]
            in_num = nums[i]
            balance = 0
            # case where out num wasnt in lo
            if out_num > -lo[0]:
                balance -= 1
            else:
                balance += 1
            counts[out_num] += 1

            if in_num > -lo[0]:
                balance += 1
                heapq.heappush(hi, in_num)
            else:
                balance -= 1
                heapq.heappush(lo, -in_num)

            # hi has too much 
            if balance > 0:
                from_hi = heapq.heappop(hi)
                heapq.heappush(lo, -from_hi)
                balance = 0
            elif balance < 0:
                from_lo = heapq.heappop(lo)
                heapq.heappush(hi, -from_lo)
                balance = 0
            
            while (lo and counts[-lo[0]] > 0):
                counts[-lo[0]] -= 1
                heapq.heappop(lo)
            while (hi and counts[hi[0]] > 0):
                counts[hi[0]] -= 1
                heapq.heappop(hi)
            
            res.append(getMedian(lo, hi, k))

        return res

