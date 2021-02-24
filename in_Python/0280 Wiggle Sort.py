class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i = 1
        while i < len(nums)-1:
            t = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = t
            i += 2
        
    