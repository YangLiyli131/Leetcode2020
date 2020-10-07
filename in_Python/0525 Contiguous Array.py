class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        s = 0
        d = {}
        d[0] = -1
        for i in range(len(nums)):
            x = nums[i]
            if x == 1:
                s += 1
            else:
                s -= 1
            if s in d:
                res = max(res, i - d[s])
            else:
                d[s] = i
        return res
        