class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x : x[0])
        def overlap(a,b):
            return a[0] <= b[1] and b[0] <= a[1]
        def merge(a,b):
            return [min(a[0],b[0]), max(a[1],b[1])]
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if overlap(res[-1], cur):
                res[-1] = merge(res[-1], cur)
            else:
                res.append(cur)
        return res
        