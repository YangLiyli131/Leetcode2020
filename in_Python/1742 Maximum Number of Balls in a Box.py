class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        d = {}
        
        def check(x):
            r = 0
            while x != 0:
                r += x % 10
                x /= 10
            return r
        
        for i in range(lowLimit, highLimit+1):
            n = check(i)
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        res = 0
        for k in d:
            res = max(res, d[k])
        return res