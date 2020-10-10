class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        f = -1
        fm = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            if d[i] > f:
                f = d[i]
        for k in d:
            if d[k] == f:
                fm.append(k)
        res = 50001
        for f in fm:
            i,j = 0,0
            for i in range(len(nums)):
                if nums[i] == f:
                    break
            for j in range(len(nums)-1, -1,-1):
                if nums[j] == f:
                    break
            res = min(res, j-i+1)
        return res