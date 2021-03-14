class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.Counter(nums)
        for k in d:
            if d[k] == 1:
                r = k
                break
        return r