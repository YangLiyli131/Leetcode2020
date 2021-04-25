class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        r = 0
        for x in costs:
            if x <= coins:
                coins -= x
                r += 1
        return r