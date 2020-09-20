class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            n = nums[i]
            idx = index[i]
            res.insert(idx,n)
        return res