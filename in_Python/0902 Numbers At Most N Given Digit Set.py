class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        sn = str(n)
        L = len(sn)
        N = len(digits)
        res = 0
        for i in range(1,L):
            res += N ** i
        i = 0
        while i < L:
            first = 0
            for x in digits:
                if x < sn[i]:
                    first += 1
            res += first * (N ** (L - i - 1))
            if sn[i] not in digits:
                break
            i += 1
        return res + (i == L)