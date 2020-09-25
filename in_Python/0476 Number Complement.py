class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        idx = 0
        while num != 0:
            c = num % 2
            num /= 2
            res += (1-c) * pow(2, idx)
            idx += 1
        return res