class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        total = sum(nums)
        x = 0
        idx = -1
        while x <= total - x:
            res.append(nums[idx])
            x += nums[idx]
            idx -= 1
        return res