class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0, len(nums)-1
        while i < j:
            m = i + (j-i)/2
            if m % 2 == 0:
                if nums[m] == nums[m+1]:
                    i = m + 2
                else:
                    j = m
            else:
                if nums[m] == nums[m-1]:
                    i = m + 1
                else:
                    j = m
        return nums[i]