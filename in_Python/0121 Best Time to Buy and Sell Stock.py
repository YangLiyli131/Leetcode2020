class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if prices == None or len(prices) == 0:
            return res
        curmin = prices[0]
        for i in range(1, len(prices)):
            p = prices[i]
            if p < curmin:
                curmin = p
            else:
                dis = p - curmin
                if dis > res:
                    res = dis
        return res