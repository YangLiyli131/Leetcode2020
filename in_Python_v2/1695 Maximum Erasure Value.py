class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0, 1
        r = nums[0]
        d = set()
        d.add(nums[i])
        cs = nums[i]
        while j < len(nums):
            if nums[j] not in d:
                d.add(nums[j])
                cs += nums[j]
                j += 1            
                r = max(r, cs)
            else:
                while i < j and nums[j] in d:
                    d.remove(nums[i])
                    cs -= nums[i]
                    i += 1
        
        return r