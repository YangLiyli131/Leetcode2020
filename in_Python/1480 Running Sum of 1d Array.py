class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums
        for i in range(1, len(nums)):
            res[i] = res[i-1] + nums[i]
        return res