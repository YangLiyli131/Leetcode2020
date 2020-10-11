class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        res.append(A[0] == 0)
        for i in range(1,len(A)):
            cur = A[i-1] * 2 + A[i]
            res.append(cur % 5 == 0)
            A[i] = cur
        return res
        