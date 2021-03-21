class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = -sys.maxint
        i = 0
        while i < len(nums):
            cur = nums[i]
            j = i + 1
            pre = i
            while j < len(nums):
                if nums[j] > nums[pre]:
                    cur += nums[j]
                    pre = j
                    j += 1
                else:
                    break
            r = max(r, cur)
            i = j
        return r
                    
                