class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc, dec = [1],[1]
        for i in range(1, len(nums)):
            ic = inc[-1]
            if nums[i] > nums[i-1]:
                t = dec[-1] + 1
                ic = max(ic, t)
            
            dc = dec[-1]
            if nums[i] < nums[i-1]:
                t = inc[-1] + 1
                dc = max(dc, t)
            
            inc.append(ic)
            dec.append(dc)
        return max(dec[-1], inc[-1])