class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x != 0 and y != 0:
            a = x % 2
            b = y % 2
            if a != b: 
                res += 1
            x /= 2
            y /= 2
        while x == 0 and y != 0:
            res += y % 2
            y /= 2
        while x != 0 and y == 0:
            res += x % 2
            x /= 2    
        return res