class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = [0] * (total+1)
        dp[0] = 1
        for n in nums:
            for i in range(total, -1, -1):
                if dp[i]:
                    dp[i+n] = 1
            if dp[total/2] == 1:
                return True
        return False
        