class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        while i < len(nums) and nums[i] != 1:
            i += 1
        first = i
        last = first + 1
        while last < len(nums):
            while last < len(nums) and nums[last] != 1:
                last += 1
            if last < len(nums):
                d = last - first - 1
                if d < k:
                    return False
            first = last
            last = first + 1
        return True
        