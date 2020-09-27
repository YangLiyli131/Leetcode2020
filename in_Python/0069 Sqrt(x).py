class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1
        j = x/2
        if x == 1:
            return 1
        while i+1 < j:
            m = (j - i)/2 + i
            if m*m < x:
                i = m
            else:
                j = m
        if j * j <= x:
            return j
        else:
            return i
        