class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        res = 0
        for k in d:
            if k + 1 in d:
                res = max(res, d[k] + d[k+1])
        return res