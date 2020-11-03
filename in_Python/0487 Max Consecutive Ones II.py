class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i,j = 0,0
        counter = 0
        while j < len(nums):
            while j < len(nums) and counter < 1:
                if nums[j] == 0:
                    counter += 1
                j += 1
            while j < len(nums) and nums[j] == 1:
                j += 1
            res = max(res, j-i)
            while i < len(nums) and nums[i] == 1:
                i += 1
            i += 1
            counter -= 1
        return res