class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        cur = ""
        if n == 0:
            return '0'
        while n != 0:
            cur = str(n % 10) + cur
            if len(cur) % 3 == 0:
                res = '.' + cur + res
                cur = ""
            n /= 10
        res = cur + res
        if res[0] == '.':
            res = res[1:]
        return res
        