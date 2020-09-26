class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i <= j:
            m = i + (j-i) / 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                j = m - 1
            else:
                i = m + 1
        return -1