class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        back = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while n != 0:
            re = n % 26
            res = back[re-1] + res
            n /= 26
            if re == 0:
                n -= 1
        return res
            