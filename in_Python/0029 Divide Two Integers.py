class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend == 0:
            return 0
        if dividend > 0 and divisor < 0:
            sign = -1
        if dividend < 0 and divisor > 0:
            sign = -1
        x = abs(dividend)
        y = abs(divisor)
        res = 0
        while x >= y:
            temp, inc = y, 1
            while x >= temp:
                x -= temp
                res += inc
                inc = inc + inc
                temp = temp + temp
            
        if sign == -1:
            res = -res
        return min(max(-2147483648, res), 2147483647)