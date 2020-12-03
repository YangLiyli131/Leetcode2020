class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        winsum = 0
        lo = -1
        size = -1
        n = len(nums)
        for hi, num in enumerate(nums):
            winsum += num
            while lo < n - 1 and winsum > target:
                lo += 1
                winsum -= nums[lo]
            if winsum == target:
                size = max(size, hi - lo)
        if size < 0:
            return -1
        return n - size
        
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        res = sys.maxint
        d1 = {}
        d2 = {}
        d1[nums[0]] = 1
        d2[nums[-1]] = 1
        xx = nums[:]
        for i in range(1, len(nums)):
            xx[i] += xx[i-1]
            d1[xx[i]] = i+1
        xx = nums[:]
        for i in range(len(nums)-2, -1, -1):
            xx[i] += xx[i+1]
            d2[xx[i]] = len(nums)-i
        for k in d1:
            left = d1[k]
            if k == x:
                res = min(res, left)
            if x - k in d2:
                right = d2[x-k]
                if left + right <= len(nums):
                    res = min(res, left+right)
        for k in d2:
            right = d2[k]
            if k == x:
                res = min(res, right)
            if x - k in d1:
                left = d1[x-k]
                if left + right <= len(nums):
                    res = min(res, left+right)
        if res == sys.maxint:
            return -1
        return res