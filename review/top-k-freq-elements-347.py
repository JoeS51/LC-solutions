class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        m = defaultdict(int)
        for num in nums:
            m[num] += 1

        hq = []
        heapq.heapify(hq)

        for key, val in m.items():
            heapq.heappush(hq, (-val, key))
        while k > 0:
            k -= 1
            (val, key) = heapq.heappop(hq)
            res.append(key)
        return res

# time complexity = O(nlogn)
# space complexity = O(n)
