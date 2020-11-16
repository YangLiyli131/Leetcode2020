class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        if nums == None or len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]
        if lower < nums[0]:
            res.append([lower, nums[0]-1])
        for j in range(1, len(nums)):
            a = nums[j-1]
            b = nums[j]
            if a + 1 < b:
                res.append([a+1, b-1])
        if upper > nums[-1]:
            res.append([nums[-1]+1,upper])
        result = []
        for x in res:
            if x[0] == x[1]:
                result.append(str(x[0]))
            else:
                result.append(str(x[0]) + '->' + str(x[1]))
        return result
            