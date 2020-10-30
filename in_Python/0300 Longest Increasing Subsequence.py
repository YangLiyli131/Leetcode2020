class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            cur = nums[i]
            curres = 1
            for j in range(i-1, -1, -1):
                if nums[j] < cur:
                    curres = max(curres, dp[j]+1)
            dp[i] = curres
            res = max(res, dp[i])
        return res
        