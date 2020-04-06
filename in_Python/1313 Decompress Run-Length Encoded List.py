class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(1,len(nums),2):
            a = nums[i-1]
            b = nums[i]
            while a != 0:
                res.append(b)
                a -= 1
        return res