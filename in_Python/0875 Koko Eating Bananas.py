class Solution(object):
    def able(self, piles, m, H):
        res = 0
        for p in piles:
            if p % m == 0:
                res += 1
            else:
                res += p / m + 1
        return res <= H
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        t = sum(piles)
        i = (t + H-1) / H
        j = t
        while i < j:
            m = i + (j-i) / 2
            if self.able(piles, m, H):
                j = m
            else:
                i = m + 1
        return j