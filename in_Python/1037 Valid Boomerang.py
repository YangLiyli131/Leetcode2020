class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        a1 = points[0][0]
        b1 = points[0][1]
        a2 = points[1][0]
        b2 = points[1][1]
        a3 = points[2][0]
        b3 = points[2][1]
        c1 = a2 - a1
        c2 = a3 - a1
        d1 = b2 - b1
        d2 = b3 - b1
        if d1 * c2 == d2 * c1:
            return False
        return True
            