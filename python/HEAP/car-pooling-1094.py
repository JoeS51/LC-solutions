class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        end_times = []
        sorted_trips = sorted(trips, key= lambda x: x[1])

        for i in range(len(sorted_trips)):
            curr_cap, start, end = sorted_trips[i]
            while end_times and end_times[0][0] <= start:
                popped_end, popped_start, popped_cap = heapq.heappop(end_times)
                capacity += popped_cap
            if capacity < curr_cap:
                return False
            capacity -= curr_cap
            heapq.heappush(end_times,(end, start, curr_cap))
        return True
        

