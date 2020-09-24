class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        idx = 0
        k = 1
        if len(nums) <=1 :
            return len(nums)
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
                k += 1
            t = nums[i]
            k = min(k, 2)
            while k >= 1:
                nums[idx] = t
                idx += 1
                k -= 1
            i = j
        return idx