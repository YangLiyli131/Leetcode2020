class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j = 0, len(nums)-1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return j+1
        while i < j:
            m = i + (j-i)/2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m
        return i
        