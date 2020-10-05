class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        nums.sort(cmp = lambda a, b : cmp(a+b, b+a), reverse = True)
        return str(int(''.join(nums)))
        