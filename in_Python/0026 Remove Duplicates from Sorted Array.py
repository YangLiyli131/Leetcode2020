class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        idx = 0
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            nums[idx] = nums[i]
            i = j
            idx += 1
        return idx