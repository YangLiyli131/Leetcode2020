class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if nums[idx] >= 0:
                nums[idx] = -nums[idx]
            else:
                # if it is negative, means the index has shown already
                res.append(idx+1)
        return res
        