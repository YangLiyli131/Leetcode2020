class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(prices)):
            curp = prices[i]
            dis = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= curp:
                    dis = prices[j]
                    break
            res.append(curp - dis)
        return res
        