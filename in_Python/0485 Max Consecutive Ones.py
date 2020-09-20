class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        start = 0
        while start < len(nums):
            while start < len(nums) and nums[start] == 0:
                start = start + 1
            end = start
            while end < len(nums) and nums[end] == 1:
                end = end + 1
            res = max(res, end - start)
            start = end
        return res