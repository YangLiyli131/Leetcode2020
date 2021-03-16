class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy,sell = [],[]
        buy.append(-prices[0] - fee)
        sell.append(0)
        for p in prices[1:]:
            b = sell[-1] - p - fee
            s = buy[-1] + p
            buy.append(max(buy[-1], b))
            sell.append(max(sell[-1], s))
        return max(sell[-1],buy[-1])