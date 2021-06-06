class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        r = 0
        for x in s:
            if x - 1 not in s:
                c = 1
                n = x
                while n + 1 in s:
                    c += 1
                    n += 1
                r = max(r, c)
        return r