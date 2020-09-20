class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        i = 0
        j = n
        while j < len(nums):
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        return res