class Solution(object):
    def check(self, nums, x):
        res = 0
        for i in nums:
            res += (i + x - 1) / x
        return res
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        i = 1
        j = max(nums)
        while i < j:
            m = i + (j-i) / 2
            if self.check(nums,m) > threshold:
                i = m + 1
            else:
                j = m
        return i