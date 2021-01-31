class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nh, h, nhc = 0, -sys.maxint, -sys.maxint
        for p in prices:
            h, nh, nhc = max(h, nh - p), max(nh,nhc), h + p
        return max(nh, max(h,nhc))