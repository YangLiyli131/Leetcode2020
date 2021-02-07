class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = nums[:]
        a.sort()
        x = nums + nums
        n = len(nums)
        def check(a,b):
            return tuple(a) == tuple(b)
        
        for i in range(n):
            cur = x[i : i + n]
            if check(cur, a):
                return True
        return False