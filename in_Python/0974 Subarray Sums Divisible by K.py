class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        r = 0
        pre = 0
        c = [1] + [0] * K
        for a in A:
            pre = (pre + a) % K
            r += c[pre]
            c[pre] += 1
        return r
        