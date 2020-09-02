class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        res = 0
        for i in range(len(nums)):
            k = nums[i]
            if k not in dict:
                t = []
                t.append(i)
                dict[k] = t
            else:
                t = dict[k]
                t.append(i)
                dict[k] = t
        for k in dict:
            v = len(dict[k])
            res += v * (v-1) / 2
        return res
        