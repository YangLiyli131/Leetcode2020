class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        res = -sys.maxint
        for x in n:
            xi = int(x)
            res = max(xi,res)
        return res