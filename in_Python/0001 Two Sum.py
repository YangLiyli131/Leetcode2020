class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in dict:
                res.append(i)
                res.append(dict[target - nums[i]])
                break
            else:
                dict[nums[i]] = i
        return sorted(res)
        