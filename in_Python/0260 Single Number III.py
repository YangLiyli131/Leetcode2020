class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d.pop(x, None)
        return list(d.keys())