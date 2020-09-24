class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        intMax = 2147483647
        intMin = -2147483648
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        n = 0
        while x != 0:
            n = n * 10 + x % 10
            x /= 10
        r = sign * n
        if r > intMax or r < intMin:
            return 0
        else:
            return r