class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key = lambda x : x[0])
        res = 0
        for i in range(1, len(points)):
            cur = points[i][0]
            pre = points[i-1][0]
            if cur > pre:
                res = max(res, cur-pre)
        return res
        