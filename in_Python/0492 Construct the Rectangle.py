class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        m = int(sqrt(area))
        if m * m == area:
            return [m,m]
        while area % m != 0:
            m -= 1
        return [area/m,m]