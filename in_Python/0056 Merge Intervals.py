class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == None or len(intervals) == 0:
            return []
        def overlap(a,b):
            return a[0] <= b[1] and b[0] <= a[1]
        def merge(a,b):
            return [min(a[0],b[0]), max(a[1],b[1])]
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if overlap(res[-1], intervals[i]):
                res[-1] = merge(res[-1],intervals[i])
            else:
                res.append(intervals[i])
        return res