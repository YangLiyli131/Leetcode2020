class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if intervals == None or len(intervals) == 0:
            return True
        intervals = sorted(intervals, key = lambda x: x[0])
        def overlap(a, b):
            return a[0] < b[1] and b[0] < a[1]
        arr = [intervals[0]]
        for i in range(1, len(intervals)):
            pre = arr[-1]
            cur = intervals[i]
            if overlap(pre, cur):
                return False
            arr.append(cur)
        return True