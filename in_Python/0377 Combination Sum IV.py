class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, len(dp)):
            cur = 0
            for x in nums:
                if i - x >= 0:
                    cur += dp[i-x]
            dp[i] = cur
        return dp[-1]