class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] > m:
                m = nums[i]
                idx = i
        for i in nums:
            if i != m and (i + i) > m:
                return -1
        return idx
        