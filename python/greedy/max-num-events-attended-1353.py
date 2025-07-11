# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# 
# You can attend an event i at any day d where startDayi <= d <= endDayi. You can only attend one event at any time d.
# 
# Return the maximum number of events you can attend.
# 
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# Example 2:
# 
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        sorted_events = sorted(events, key = lambda x: (x[0], x[1]))
        max_day = max(event[1] for event in events)
        pq = []

        j = 0
        res = 0
        for day in range(1, max_day + 1):
            while j < len(sorted_events) and sorted_events[j][0] <= day:
                heapq.heappush(pq, sorted_events[j][1])
                j += 1
            while pq and pq[0] < day:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                res += 1
        return res

        
# runtime: O(nlogn)
# spacetime: O(n)
