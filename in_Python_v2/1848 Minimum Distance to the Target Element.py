class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        r = sys.maxint
        for i, n in enumerate(nums):
            if n == target:
                r = min(r, abs(i - start))
        return r