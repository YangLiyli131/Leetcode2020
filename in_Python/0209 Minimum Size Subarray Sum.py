class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i,j,res = 0,0,sys.maxint
        cur = 0
        while j < len(nums):
            cur += nums[j]
            while cur >= s:
                res = min(res, j - i + 1)
                cur -= nums[i]
                i += 1
            j += 1
        if res == sys.maxint:
            return 0
        return res
            

class Solution(object):
    def bs(self, i, j, tar, A):
        while i <= j:
            m = i + (j-i)/2
            if A[m] < tar:
                i = m + 1
            else:
                j = m - 1
        return i
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        arr = [0]
        for x in nums:
            arr.append(arr[-1] + x)
        res = sys.maxint
        for i in range(0,len(arr)):
            j = self.bs(i+1, len(arr)-1, arr[i]+s, arr)
            if j == len(arr):
                break
            res = min(res, j-i)
        if res == sys.maxint:
            return 0
        return res