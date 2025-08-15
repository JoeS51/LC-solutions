class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        if k == 1 and len(order) == 1:
            return 0

        def validSubstrings(t):
            idx = sorted(order[:t+1])
            window = 0
            n = len(s)
            total = (n * (n+1)) // 2
            curr_idx = 0
            for i in range(len(s)):
                if curr_idx >= len(idx) or i != idx[curr_idx]:
                    window += 1
                else:
                    curr_idx += 1
                    invalid_strings = ((window) * (window+1)) // 2
                    total -= invalid_strings
                    window = 0
            if window > 0:
                total -= (((window) * (window+1)) // 2)
            return total >= k

        lo, hi = 0, len(order)
        while lo < hi:
            mid = (lo + hi) // 2
            if validSubstrings(mid):
                hi = mid
            else:
                lo = mid + 1
        if lo == len(order):
            return -1
        return lo
        
# runtime: O(NLOGN)
# spacetime: O(NLOGM) where m is length of order
