class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p % 2 == 0 and q % 2 == 0:
            q /= 2
            p /= 2
        return 1 - p % 2 + q % 2