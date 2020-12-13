class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = []
        left = [0,nums[0]]
        right = [nums[-1],0]
        for i in range(1,N):
            cur = nums[i] + left[-1]
            left.append(cur)
        for i in range(N-2, -1, -1):
            cur = nums[i] + right[0]
            right.insert(0,cur)
        for i in range(N):
            numleft = i
            numright = N - i - 1
            t = nums[i] * numleft - left[i] + right[i+1] - nums[i] * numright
            res.append(t)
        return res