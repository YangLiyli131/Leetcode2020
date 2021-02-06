class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.Counter(nums)
        r = 0
        for k in d:
            if d[k] == 1:
                r += k
        return r