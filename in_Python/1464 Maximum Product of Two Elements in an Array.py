class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sorted(nums)
        return (x[len(nums)-1]-1) *(x[len(nums)-2]-1)
        