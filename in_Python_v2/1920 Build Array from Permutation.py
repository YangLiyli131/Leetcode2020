class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for i, x in enumerate(nums):
            r.append(nums[nums[i]])
        return r