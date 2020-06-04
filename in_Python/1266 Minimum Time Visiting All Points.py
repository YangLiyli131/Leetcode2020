class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        a = points[0][0]
        b = points[0][1]
        for i in range(1,len(points)):
            aa = points[i][0]
            bb = points[i][1]
            res += max(abs(aa-a),abs(bb-b))
            a = aa
            b = bb
        return res