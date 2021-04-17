class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur <= nums[i-1]:
                r += nums[i-1] - cur + 1
                nums[i] = nums[i-1] + 1
        return r