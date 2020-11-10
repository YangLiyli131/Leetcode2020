class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        d = {1:1,6:9,9:6,0:0,8:8}
        res = 0
        x = N
        while x:
            y = x % 10
            if y not in d:
                return False
            res = res * 10 + d[y]
            x /= 10
        return res != N