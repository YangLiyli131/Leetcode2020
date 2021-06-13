class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        r = 0
        i,j = 0, len(nums)-1
        while i < j:
            r = max(nums[i] + nums[j], r)
            i += 1
            j -= 1
        return r