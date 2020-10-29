class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        a1,b1,a2,b2 = rec1[0],rec1[1],rec1[2],rec1[3]
        a3,b3,a4,b4 = rec2[0],rec2[1],rec2[2],rec2[3]
        f1 = False
        f2 = False
        if max(a1,a3) < min(a2,a4):
            f1 = True
        if max(b1,b3) < min(b2,b4):
            f2 = True
        return f1 and f2