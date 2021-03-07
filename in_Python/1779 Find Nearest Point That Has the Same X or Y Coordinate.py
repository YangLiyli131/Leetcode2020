class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        r = sys.maxint
        res = -1
        for pi in range(len(points)):
            p = points[pi]
            a,b = p[0], p[1]
            if a == x or b == y:
                d = (a-x)*(a-x) + (b-y)*(b-y)
                if d < r:
                    r = d
                    res = pi
                elif d == r:
                    res = min(res, pi)
        return res