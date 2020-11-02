class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if intervals == None or len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda x : x[0])
        res = 1
        q = []
        heapq.heappush(q, intervals[0][1])
        for i in range(1, len(intervals)):
            begintime = intervals[i][0]
            early = heapq.heappop(q)
            if early <= begintime:
                heapq.heappush(q,intervals[i][1])
            else:
                res += 1
                heapq.heappush(q,early)
                heapq.heappush(q,intervals[i][1])
        return res