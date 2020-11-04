class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l,r = 0, len(A)-1
        while l < r:
            m = l + (r-l)/2
            if A[m] - m < 0:
                l = m + 1
            else:
                r = m
        if A[l] == l:
            return l
        return -1