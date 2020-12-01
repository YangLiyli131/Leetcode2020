class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        t = nums[len(nums)/2]
        res = 0
        for n in nums:
            res += abs(n-t)
        return res