class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        idx = 0
        if N == 0:
            return 1
        while N != 0:
            c = N % 2
            N /= 2
            res += (1 - c) * pow(2, idx)
            idx += 1
        return res
        