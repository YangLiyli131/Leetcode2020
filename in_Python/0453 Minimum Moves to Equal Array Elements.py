class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) <= 1:
            return 0
        nums.sort()
        mm = nums[0]
        s = sum(nums)
        n = len(nums)
        return s - mm * n