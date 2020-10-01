class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        if nums[0] <= 0 or nums[-1] >= 0:
            return nums[0] * nums[1] * nums[2]
        else:
            a = nums[0] * nums[1] * nums[2]
            b = nums[0] * nums[-1] * nums[-2]
            return max(a,b)