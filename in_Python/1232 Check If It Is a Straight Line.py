class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        a1 = coordinates[0][0]
        a2 = coordinates[0][1]
        b1 = coordinates[1][0]
        b2 = coordinates[1][1]
        for c in range(2, len(coordinates)):
            c2 = coordinates[c][1]
            c1 = coordinates[c][0]
            if (b2-a2) * (c1-a1) != (b1-a1) * (c2-a2):
                return False
        return True