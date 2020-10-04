class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s,e = i+1, len(nums)-1
            t = -nums[i]
            while s < e:
                if nums[s] + nums[e] == t:
                    res.append([nums[i],nums[s],nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                elif nums[s] + nums[e] < t:
                    s += 1
                else:
                    e -= 1
        return res
    