class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mm = nums[0]
        cursum = nums[0]
        for i in range(1, len(nums)):
            cursum += nums[i]
            mm = min(mm, cursum)
        #print(mm)
        return abs(min(0, mm)) + 1
        