class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.append(1)
        nums.insert(0,1)
        c = [[0] * (n+2) for __ in range(n+2)]
        for l in range(1, n+1):
            for i in range(1, n-l+2):
                j = i - 1 + l
                for k in range(i,j+1):
                    c[i][j] = max(c[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + c[k+1][j], c[i][j])
        return c[1][n]