class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums
        L = sorted(nums)
        for i in range(len(L)):
            res[i] = L.index(nums[i])        
        return res
        