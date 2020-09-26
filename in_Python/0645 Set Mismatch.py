class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)+1
        d = {}
        res = [0,0]
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                res[0] = i
                d[i] = 1
        for i in range(1,n):
            if i not in d:
                res[1] = i
                break
        return res