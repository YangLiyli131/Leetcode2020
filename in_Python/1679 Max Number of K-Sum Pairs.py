class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        nums.sort()
        i,j = 0, len(nums)-1
        while i < j:
            left = nums[i]
            right = nums[j]
            if left + right == k:
                res += 1
                i += 1
                j -= 1
            elif left + right < k:
                i += 1
            else:
                j -= 1
        return res