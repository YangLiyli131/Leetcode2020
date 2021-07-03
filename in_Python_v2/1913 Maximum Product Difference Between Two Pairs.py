class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = nums
        x.sort()
        return x[-1] * x[-2] - x[1] * x[0]