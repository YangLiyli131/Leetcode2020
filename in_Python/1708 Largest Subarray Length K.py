class Solution(object):
    def largestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        idx = -1
        curmax = -sys.maxint
        for i in range(len(nums) - k + 1):
            c = nums[i]
            if c > curmax:
                curmax = c
                idx = i
        return nums[idx : idx + k]