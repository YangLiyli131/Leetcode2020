class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        dp = []
        dp.append(0)
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(dp[-2]+nums[i], dp[-1]))
        return dp[-1]
        