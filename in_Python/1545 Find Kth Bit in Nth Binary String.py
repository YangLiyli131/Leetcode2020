class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        l = 2 ** n - 1
        flip = 0
        while k > 1:
            if k == l/2 + 1:
                return str(1 ^ flip)
            if k > l/2:
                k = l + 1 - k
                flip = 1 - flip
            l /= 2
        return str(flip)