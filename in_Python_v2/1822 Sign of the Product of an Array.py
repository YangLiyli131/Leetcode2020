class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        r = 0
        for x in nums:
            if x < 0:
                r += 1
        if r % 2 == 0:
            return 1
        return -1