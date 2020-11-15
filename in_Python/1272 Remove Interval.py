class Solution(object):
    def overlap(self, a, b):
        return a[0] < b[1] and b[0] < a[1]
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for it in intervals:
            if not self.overlap(it, toBeRemoved):
                res.append(it)
                continue
            x0 = toBeRemoved[0]
            x1 = toBeRemoved[1]
            a0 = it[0]
            a1 = it[1]
            if a0 >= x0 and a1 <= x1:
                continue
            elif a0 < x0 and a1 > x1:
                res.append([a0, x0])
                res.append([x1, a1])
            elif a0 < x0 and x0 <= a1 < x1:
                res.append([a0, x0])
            elif x0 <= a0 < x1 and x1 < a1:
                res.append([x1, a1])
        return res