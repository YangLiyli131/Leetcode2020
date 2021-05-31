class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        r = 0
        for i in range(1, len(nums)):
            r = max(r, nums[i] - nums[i-1])
        return r