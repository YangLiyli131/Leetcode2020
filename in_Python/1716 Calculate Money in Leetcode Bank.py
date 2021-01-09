class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        weeks = n / 7
        remain = n % 7
        for i in range(1, weeks+1):
            res += (i + i + 6) * 7 / 2
        start = weeks + 1
        while remain != 0:
            res += start
            start += 1
            remain -= 1
        return res