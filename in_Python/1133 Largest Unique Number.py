class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}
        for a in A:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
        res = -1
        for k in d:
            if d[k] == 1:
                res = max(res, k)
        return res