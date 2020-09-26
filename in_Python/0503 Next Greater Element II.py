class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.append(-1)
        idx = []
        v = []
        for i in range(len(nums) * 2):
            if i >= len(nums):
                curv = nums[i - len(nums)]
            else:
                curv = nums[i]
            while len(v) != 0 and curv > v[-1]:
                newidx = idx.pop()
                v.pop()
                if newidx < len(nums):
                    res[newidx] = curv
            idx.append(i)
            v.append(curv)
        return res
                
                
            