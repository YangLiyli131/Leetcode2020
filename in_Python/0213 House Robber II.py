class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(arr):
            if arr == None or len(arr) == 0:
                return 0
            N = len(arr)
            dp = [0] * (N+1)
            dp[1] = arr[0]
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i-1])
            return dp[-1]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        arr1 = nums[0:n-1]
        arr2 = nums[1:]
        x1 = helper(arr1)
        x2 = helper(arr2)
        return max(x1,x2)