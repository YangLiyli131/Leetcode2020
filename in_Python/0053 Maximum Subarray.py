class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        #print(nums)
        curmin = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            res = max(res, nums[i] - curmin)
            res = max(res, nums[i])
            if curmin > nums[i]:
                curmin = nums[i]
        return res

        