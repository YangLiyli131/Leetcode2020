class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        m = n/2
        nv = 1
        while m != 0:
            res.append(nv)
            res.append(-nv)
            nv += 1
            m -= 1
        if n % 2 == 1:
            res.append(0)
        return res
        