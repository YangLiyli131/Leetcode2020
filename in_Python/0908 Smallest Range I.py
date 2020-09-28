class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        newlow = A[0] + K
        newhigh = A[-1] - K
        return max(newhigh - newlow, 0)