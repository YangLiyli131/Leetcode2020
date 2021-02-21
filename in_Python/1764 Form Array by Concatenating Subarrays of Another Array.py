class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        
        def f(arr, t):
            if not arr:
                return -1
            n = len(t)
            for i in range(len(arr)-n+1):
                if arr[i : i+n] == t:
                    return i
            return -1
        
        for x in groups:
            r = f(nums, x)
            if r == -1:
                return False
            nums = nums[r+len(x):]
        return True