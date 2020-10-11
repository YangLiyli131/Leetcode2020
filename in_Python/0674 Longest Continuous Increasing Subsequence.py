class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        res = 1
        i,j = 0,1
        while j < len(nums):
            while j < len(nums) and nums[j] > nums[j-1]:
                j += 1
            res = max(res, j-i)
            i = j
            j = i + 1
        return res