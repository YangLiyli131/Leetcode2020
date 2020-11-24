class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        div = 0
        for i in nums:
            num_division = 0
            while i != 0:
                if i % 2 == 0:
                    i /= 2
                    num_division += 1
                else:
                    i -= 1
                    res += 1
            div = max(div, num_division)
        return res + div
        