class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = -1
        if len(A) == 1:
            return res
        A.sort()
        i,j = 0, len(A)-1
        while i < j:
            a = A[i]
            b = A[j]
            if a + b >= K:
                j -= 1
            else:
                res = max(res, a+b)
                i += 1
        return res