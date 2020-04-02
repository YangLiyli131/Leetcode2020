class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()       
        while n not in seen:
            seen.add(n)
            res = 0
            s = str(n)
            for i in list(s):
                res += int(i) ** 2
            n = res
        return n == 1
        