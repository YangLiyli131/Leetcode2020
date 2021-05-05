class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [sys.maxint] * len(nums)
        dp[0] = 0
        for i in range(len(nums)-1):
            d = nums[i]
            for j in range(i+1, min(len(nums), i+d+1)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]