class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = []
        for i in range(len(startTime)):
            intervals.append((startTime[i], endTime[i], profit[i]))
        intervals = sorted(intervals, key= lambda x: x[1])
        p = []
        p.append(-1)
        end_times = [interval[1] for interval in intervals]

        p = []
        for j in range(len(intervals)):
            start = intervals[j][0]
            # Find rightmost index where end_time <= start
            i = bisect_right(end_times, start) - 1
            p.append(i)
        print(p)
        # print(intervals)
        # print(p)
        @cache
        def dp(i):
            if i == -1:
                return 0
            return max(dp(i-1), dp(p[i]) + intervals[i][2]) 
        return dp(len(p)-1)



        

