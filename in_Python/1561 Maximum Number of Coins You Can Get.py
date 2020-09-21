class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        res = 0
        idx = -2
        times = len(piles) / 3
        while times != 0:
            res += piles[idx]
            times -= 1
            idx -= 2
        return res
            