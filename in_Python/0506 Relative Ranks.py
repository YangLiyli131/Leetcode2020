class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {}
        res = []
        for i in range(len(nums)):
            res.append('')
            d[nums[i]] = i
        nums.sort(reverse = True)
        for i in range(len(nums)):
            idx = d[nums[i]]
            if i == 0:
                res[idx] = 'Gold Medal'
            elif i == 1:
                res[idx] = 'Silver Medal'
            elif i == 2:
                res[idx] = 'Bronze Medal'
            else:
                res[idx] = str(i+1)
        return res