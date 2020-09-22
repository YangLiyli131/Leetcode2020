class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        x = numBottles
        y = numExchange
        res = x
        while x >= y:
            newBottles = x / y       
            res += newBottles
            resu = x % y
            x = newBottles + resu
        return res 
        